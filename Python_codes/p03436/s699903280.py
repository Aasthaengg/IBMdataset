import sys
from collections import deque

H, W = map(int, sys.stdin.readline().split())

grid = []
for _ in range(H):
    grid.append(sys.stdin.readline().strip())

black = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == "#":
            black += 1

q = deque()
q.append((0, 0, 0))
visited = set()
while q:
    x, y, c = q.popleft()
    if x == W-1 and y == H-1:
        break
    if (x, y) in visited:
        continue
    visited.add((x, y))

    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < W and 0 <= ny < H and grid[ny][nx] != "#":
                q.append((nx, ny, c+1))

if x == W-1 and y == H-1:
    print(H*W - black - c - 1)
else:
    print(-1)