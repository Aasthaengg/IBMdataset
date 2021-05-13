from collections import deque
from copy import deepcopy


def bfs(table, i, j, h, w):
    dq = deque()
    ans = 0
    dq.append((i, j, 0))  # x,y,distance
    table[i][j] = "#"
    while dq:
        x, y, dis = dq.popleft()
        ans = max(ans, dis)
        if x > 0 and (x - 1, y) and table[x - 1][y] != "#":
            dq.append((x - 1, y, dis + 1))
            table[x - 1][y] = "#"
        if x < h - 1 and (x + 1, y) and table[x + 1][y] != "#":
            dq.append((x + 1, y, dis + 1))
            table[x + 1][y] = "#"
        if y > 0 and (x, y - 1) and table[x][y - 1] != "#":
            dq.append((x, y - 1, dis + 1))
            table[x][y - 1] = "#"
        if y < w - 1 and (x, y + 1) and table[x][y + 1] != "#":
            dq.append((x, y + 1, dis + 1))
            table[x][y + 1] = "#"

    return ans


def main():
    h, w = [int(i) for i in input().strip().split()]
    grid = [list(input()) for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == ".":
                _grid = deepcopy(grid)
                max_path = bfs(_grid, i, j, h, w)
                ans = max(ans, max_path)

    print(ans)


if __name__ == "__main__":
    main()
