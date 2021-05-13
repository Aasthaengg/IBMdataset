import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())
grid = [["#"] * (W+2)]
for _ in range(H):
    grid.append(list("#" + sys.stdin.readline().strip() + "#"))
grid.append(["#"] * (W+2))
# print(grid)

q = deque()
for j in range(1, H+1):
    for i in range(1, W+1):
        if grid[j][i] == "#":
            q.append((i, j, 0))

ans = 0
while q:
    x, y, count = q.popleft()
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        if grid[y+dy][x+dx] != ".":
            continue
        grid[y+dy][x+dx] = count + 1
        ans = count + 1
        q.append((x+dx, y+dy, count + 1))

# print(grid)
print(ans)