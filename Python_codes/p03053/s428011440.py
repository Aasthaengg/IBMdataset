import sys
input = sys.stdin.readline

h,w = map(int,input().split())
c = []
for i in range(h):
  a = input()
  c.append(a)
  
from collections import deque

d = [[-1] * w for i in range(h)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

que = deque([])
for i in range(h):
  for j in range(w):
    if c[i][j] == '#':
      que.append((i,j,0))
      d[i][j] = 0

ans = 0
while que:
  p = que.popleft()
  for i in range(4):
      nw = p[1] + dx[i]
      nh = p[0] + dy[i]
      if 0 <= nw < w and 0 <= nh < h and d[nh][nw]==-1:
          que.append((nh,nw,p[2]+1))
          d[nh][nw] = p[2]+1
          ans = max(ans,p[2]+1)

print(ans)