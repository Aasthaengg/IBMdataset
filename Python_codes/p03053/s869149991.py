import sys
from collections import deque as dq
input = sys.stdin.readline
H, W = map(int, input().split())
a = [list(input())[: -1] for _ in range(H)]
dist = [[H * W] * W for _ in range(H)]
Q = dq([])
for i in range(H):
  for j in range(W):
    if a[i][j] == "#":
      Q.append((i, j))
      dist[i][j] = 0

d = [-1, 0, 1, 0]
while len(Q):
  y, x = Q.popleft()
  for k in range(4):
    u = y + d[k]
    v = x + d[-1 - k]
    if u in range(H) and (v in range(W)):
      if dist[u][v] > dist[y][x] + 1:
        dist[u][v] = dist[y][x] + 1
        Q.append((u, v))
print(max([max(dist[i]) for i in range(H)]))