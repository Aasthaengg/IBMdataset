from collections import deque
import numpy as np

H, W = map(int, input().split())
grid = [input() for _ in range(H)]
ans = 0

INF = -1
dist = [[INF for i in range(W)] for j in range(H)]

q = deque([(0, 0)])
dist[0][0] = 0

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)

while q:
    y, x = q.popleft()
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]

        if (ny < 0 or ny >= H or nx < 0 or nx >= W): continue
        if grid[ny][nx] == "#": continue
        if dist[ny][nx] != INF: continue

        dist[ny][nx] = dist[y][x] + 1
        q.append((ny, nx))

block = 0
for h in range(H):
    block += grid[h].count("#")



if dist[H-1][W-1] == INF:
    print(-1)
    exit()
else:
    ans = (H * W) - block - (dist[H-1][W-1] + 1)
    print(ans)

