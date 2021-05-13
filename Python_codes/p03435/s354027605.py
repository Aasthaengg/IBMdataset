import itertools
def main():
    grid = [list(map(int, input().split())) for i in range(3)]
    all = sum(sum(grid, []))
    a = [0] * 3
    b = [0] * 3
    for i, j, k in itertools.product(range(grid[0][0] + 1), range(grid[1][1] + 1), range(grid[2][2] + 1)):
        a = [i, j, k]
        b = [grid[idx][idx] - v for idx, v in enumerate(a)]
        if (sum(a) * 3) + (sum(b) * 3) == all:
            print("Yes")
            exit()
    print('No')


if __name__ == '__main__':
    main()
