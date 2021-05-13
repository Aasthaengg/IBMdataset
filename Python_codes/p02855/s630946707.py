import fileinput
import numpy as np


def solve(grid):

    groups = np.zeros(grid.shape, dtype=int)

    group = 0
    group_left = 0
    group_right = 0

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):

            # Continue to the next SB
            if grid[i,j] != '#':
                continue

            group = group + 1
            group_left = j
            group_right = j

            # Assign to current group
            groups[i,j] = group

            # Expand right
            for j2 in range(j + 1, grid.shape[1]):
                # Break if meet a strawberry / already assigned
                if grid[i,j2] == '#':
                    break
                if groups[i,j2] != 0:
                    break
                # Expand
                groups[i,j2] = group
                group_right = j2

            # Expand left
            for j2 in range(j - 1, -1, -1):
                # Break if meet a strawberry / already assigned
                if grid[i,j2] == '#':
                    break
                if groups[i,j2] != 0:
                    break
                # Expand
                groups[i,j2] = group
                group_left = j2

            # Expand Down
            for i2 in range(i + 1, grid.shape[0]):
                # Only expand if none of the squares are SBs or in a group already
                expand = True
                for j2 in range(group_left, group_right + 1):
                    if grid[i2,j2] == '#':
                        expand = False
                        break
                    if groups[i2,j2] != 0:
                        expand = False
                        break
                if not expand:
                    break
                for j2 in range(group_left, group_right + 1):
                    groups[i2,j2] = group

            # Expand Up
            for i2 in range(i - 1, -1, -1):
                # Only expand if none of the squares are SBs or in a group already
                expand = True
                for j2 in range(group_left, group_right + 1):
                    if grid[i2,j2] == '#':
                        expand = False
                        break
                    if groups[i2,j2] != 0:
                        expand = False
                        break
                if not expand:
                    break
                for j2 in range(group_left, group_right + 1):
                    groups[i2,j2] = group

    return groups


def main():
    grid = np.array([
        ('.', '.', '.', '.', '.', '.', '.'),
        ('#', '.', '.', '.', '#', '.', '#'),
        ('.', '.', '.', '.', '#', '.', '.'),
        ('.', '.', '#', '.', '.', '.', '#'),
        ('.', '#', '.', '.', '#', '.', '.')])
    grid = read_grid()
    # print(grid)
    groups = solve(grid)
    # print(groups)
    output_grid(groups)


def output_grid(grid):
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            print(grid[i,j], end=' ')
        print('')


def read_grid():
    grid = []
    first = True
    for line in fileinput.input():
        if first:
            first = False
            continue
        grid.append(list(line.rstrip('\n')))
    return np.array(grid)


if __name__ == '__main__':
    main()