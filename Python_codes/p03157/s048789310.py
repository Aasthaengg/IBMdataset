import sys
readline = sys.stdin.readline

H,W = map(int,readline().split())

grid = [readline().rstrip() for i in range(H)]

visited = set()
ans = 0
from collections import deque
cases = ((0,1),(0,-1),(1,0),(-1,0))
for i in range(H):
  for j in range(W):
    if (i,j) in visited:
      continue
    if grid[i][j] == ".":
      continue
    q = deque()
    black = 0
    white = 0
    q.append([i,j,1])
    aim = ".#"
    while q:
      y,x,isblack = q.popleft()
      if (y,x) in visited:
        continue
      if aim[isblack] != grid[y][x]:
        continue
      visited.add((y,x))
      if isblack:
        black += 1
      else:
        white += 1
      isblack ^= 1
      for c in cases:
        if 0 <= y + c[0] < H and 0 <= x + c[1] < W:
          q.append([y + c[0],x + c[1],isblack])
    ans += black * white
print(ans)