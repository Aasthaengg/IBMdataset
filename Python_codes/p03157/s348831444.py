import sys
from collections import deque as dq
input = sys.stdin.readline
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
d = [-1, 0, 1, 0]
vis = [[0] * W for _ in range(H)]
Q = dq([])
res = 0
for i in range(H):
  for j in range(W):
    if vis[i][j] == 1: continue
    Q.append((i, j))
    w = 0
    b = 0
    while len(Q):
      p = Q.popleft()
      if S[p[0]][p[1]] == "#": b += 1
      elif S[p[0]][p[1]] == ".": w += 1
      vis[p[0]][p[1]] = 1
      for way in range(4):
        x = p[1] + d[way]
        y = p[0] + d[-1 - way]
        if 0 <= y < H and (0 <= x < W):
          if S[p[0]][p[1]] == S[y][x]:
            continue
          if vis[y][x] == 1: continue
          Q.append((y, x))
          vis[y][x] = 1
    res += b * w
print(res)