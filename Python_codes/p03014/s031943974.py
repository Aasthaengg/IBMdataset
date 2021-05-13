import sys

H, W = map(int, sys.stdin.readline().strip().split())
grid = []
for _ in range(H):
    grid.append(sys.stdin.readline().strip())

# (x, y)のx, y方向のscore [a, b]
scores_y = [[0 for _ in range(W)] for _ in range(H)]
scores_x = [[0 for _ in range(W)] for _ in range(H)]
for y in range(H):
    start = 0
    count = 0
    for x in range(W):
        if grid[y][x] == "#" or x == W-1:
            if x == W-1 and grid[y][x] != "#":
                count += 1
            for i in range(start, x+1):
                scores_x[y][i] = count
            count = 0
            start = x + 1
        else:
            count += 1

for x in range(W):
    start = 0
    count = 0
    for y in range(H):
        if grid[y][x] == "#" or y == H-1:
            if y == H-1 and grid[y][x] != "#":
                count += 1
            for i in range(start, y+1):
                scores_y[i][x] = count
            count = 0
            start = y + 1
        else:
            count += 1

# print(scores)
ans = 0
for y in range(H):
    for x in range(W):
        ans = max(ans, scores_x[y][x] + scores_y[y][x] - 1)
print(ans)