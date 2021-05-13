from collections import*
mod=10**9+7
h,w=map(int,input().split())
a=[input() for _ in range(h)]
dx=[0,1]
dy=[1,0]
d=[[0]*w for _ in range(h)]
v=[[0]*w for _ in range(h)]
d[0][0]=1
q=deque([(0,0)])
while q:
  x,y=q.popleft()
  if v[x][y]:continue
  v[x][y]=1
  for i,j in zip(dx,dy):
    nx=x+i
    ny=y+j
    if 0<=nx<h and 0<=ny<w and a[nx][ny]==".":
      d[nx][ny]+=d[x][y]
      d[nx][ny]%=mod
      q.append((nx,ny))
print(d[-1][-1])