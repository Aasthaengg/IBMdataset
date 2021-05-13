h,w=map(int,input().split())
g=[input() for _ in range(h)]
from collections import *
def bfs(x,y):
  d=[[-1]*w for _ in range(h)]
  d[x][y]=0
  q=deque([(x,y)])
  while q:
    tx,ty=q.popleft()
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
      nx,ny=tx+dx,ty+dy
      if 0<=nx<h and 0<=ny<w and g[nx][ny]=='.' and d[nx][ny]<0:
        d[nx][ny]=d[tx][ty]+1
        q.append((nx,ny))
  return d
d=bfs(0,0)[-1][-1]
print((h*w-sum(s.count('#') for s in g)-d)*(d>0)-1)