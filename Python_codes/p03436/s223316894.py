# 白ます数 - 最短距離が答え

import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())

G = [None] * H
white = 0
for i in range(H):
  G[i] = readline().rstrip()
  white += G[i].count(".")

from collections import deque
q = deque([])
# y,x, 距離
q.append([0, 0, 0])
seen = set()
cases = ((0,1),(0,-1),(1,0),(-1,0))
while q:
  y,x,d = q.popleft()
  if G[y][x] == "#":
    continue
  if (y,x) in seen:
    continue
  seen.add((y,x))
  if y == H - 1 and x == W - 1:
    print(white - d - 1)
    break
  for c in cases:
    if 0 <= y + c[0] < H and 0 <= x + c[1] < W:
      q.append([y + c[0], x + c[1], d + 1])
else:
  print(-1)
