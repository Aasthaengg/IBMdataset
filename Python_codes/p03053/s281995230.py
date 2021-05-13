from collections import deque
INF=10**18
h,w=map(int,input().split())
e=[input() for _ in range(h)]
d=[[INF]*w for _ in range(h)]
q=deque([])
for i in range(h):
  for j in range(w):
    if e[i][j]=='#':
      q.append((i,j))
      d[i][j]=0
dx=[-1,0,1,0]
dy=[0,-1,0,1]
ans=0
while q:
  x,y=q.popleft()
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<h and 0<=ny<w and e[nx][ny]=='.' and d[nx][ny]==INF:
      q.append((nx,ny))
      d[nx][ny]=d[x][y]+1
      ans=max(d[nx][ny],ans)
print(ans)