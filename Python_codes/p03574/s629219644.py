from collections import deque
h, w = map(int, input().split())

grid = [list(input()) for _ in range(h)]

dy = (-1, -1, -1, 0, 0, 0, 1, 1, 1)
dx = (-1, 0, 1, -1, 0, 1, -1, 0, 1)

for i in range(h):
    for j, value in enumerate(grid[i]):
        if grid[i][j] == "#":
            continue
        else:
            bom_cnt = 0
            for k in range(9):
                y = i + dy[k]
                x = j + dx[k]
                if (y < 0 or y >= h or x < 0 or x >= w): continue
                if grid[i][j] == "#": continue
                if grid[y][x] == "#":
                    bom_cnt += 1

            grid[i][j] = bom_cnt

for i in range(h):
    for j in range(w):
        print(grid[i][j], end="")
    print()