import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())
S = [None] * H
for i in range(H):
  S[i] = readline().rstrip()

ans = 0
from collections import deque
cases = ((1,0),(-1,0),(0,1),(0,-1))
for i in range(H):
  for j in range(W):
    q = deque([[i,j,0]])
    seen = set()
    while q:
      y,x,d = q.popleft()
      if S[y][x] == "#":
        continue
      if (y,x) in seen:
        continue
      seen.add((y,x))
      if d > ans:
        ans = d
      for c in cases:
        if 0 <= y + c[0] < H and 0 <= x + c[1] < W:
          q.append([y + c[0], x + c[1], d + 1])

print(ans)