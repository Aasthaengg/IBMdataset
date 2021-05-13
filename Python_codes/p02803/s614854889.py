# すべてのスタートを試し、最大値の最大値を取る

import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())
grid = [readline().rstrip() for i in range(H)]

ans = 0
cases = ((0,1),(0,-1),(1,0),(-1,0))
from collections import deque
for i in range(H):
  for j in range(W):
    q = deque([[i,j,0]])
    visited = [[False] * W for i in range(H)]
    while q:
      y,x,d = q.popleft()
      if grid[y][x] == "#":
        continue
      if visited[y][x]:
        continue
      visited[y][x] = True
      if d > ans:
        ans = d
      for c in cases:
        if 0 <= y + c[0] < H and 0 <= x + c[1] < W:
          q.append([y + c[0],x + c[1],d + 1])
print(ans)