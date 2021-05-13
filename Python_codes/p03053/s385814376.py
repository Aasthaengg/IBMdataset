from collections import deque
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
A = [input().rstrip() for _ in range(H)]
dist = [[-1] * W for _ in range(H)]
queue = deque()
for i in range(H):
    for j in range(W):
        if A[i][j] == '#':
            dist[i][j] = 0
            queue.append((i, j))
while queue:
    i, j = queue.popleft()
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < H and 0 <= nj < W and dist[ni][nj] == -1:
            dist[ni][nj] = dist[i][j] + 1
            queue.append((ni, nj))
print(max(max(row) for row in dist))