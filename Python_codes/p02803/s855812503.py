ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

from collections import deque

h,w = nm()

s = []

for y in range(h):
  s.append([_ for _ in input()])



def bfs(sx,sy,visited):
  xx=[1,-1,0,0]
  yy=[0,0,1,-1]
  
  q=deque([(sx,sy)])
  visited[sy][sx] = 0

  while q:
    _ = q.popleft()
    x=_[0]
    y=_[1]

    for i in range(4):
      nx = x + xx[i]
      ny = y + yy[i]
      
      if 0 <= nx < w and 0 <= ny < h:
        if s[ny][nx] == '.' and visited[ny][nx]==-1:
          visited[ny][nx] = visited[y][x]+1
          q.append((nx,ny))
  mx=0
  for y in range(h):
    for x in range(w):
      mx = max(mx,visited[y][x])
  return mx

MX = 0

for sx in range(w):
  for sy in range(h):
    if s[sy][sx] == '.':
      b = bfs(sx,sy,[[-1]*w for _ in range(h)])
      MX = max(MX,b)

print(MX)