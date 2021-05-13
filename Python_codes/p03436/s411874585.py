from collections import deque
INF=10**18
h,w=map(int,input().split())
e=[input() for _ in range(h)]
cnt=0
for i in range(h):
  for j in range(w):
    if e[i][j]=='.':cnt+=1
dx=[-1,0,1,0]
dy=[0,-1,0,1]
sx,sy=0,0
gx,gy=h-1,w-1
q=deque([(sx,sy)])
d=[[INF]*w for _ in range(h)]
d[sx][sy]=1
while q:
  x,y=q.popleft()
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<h and 0<=ny<w and e[nx][ny]=='.' and d[nx][ny]==INF:
      q.append((nx,ny))
      d[nx][ny]=d[x][y]+1
if d[gx][gy]==INF:print(-1)
else:print(cnt-d[gx][gy])