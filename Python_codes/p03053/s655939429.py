from collections import deque

import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

H, W = map(int, input().split())
A = [input() for _ in range(H)]
dist = [-1 for _ in range(H * W)]

queue = deque()

for x in range(H):
    for y in range(W):
        if A[x][y] == '#':
            z = x * W + y
            queue.append(z)
            dist[z] = 0

while queue:
    z = queue.popleft()
    x, y = divmod(z, W)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if not (0 <= nx < H and 0 <= ny < W):
            continue
        nz = nx * W + ny
        if dist[nz] != -1:
            continue
        dist[nz] = dist[z] + 1
        queue.append(nz)

print(max(dist))