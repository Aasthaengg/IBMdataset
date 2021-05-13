import queue
INF=10**8
r,c=map(int,input().split())
#sy,sx=map(int,input().split())
#gy,gx=map(int,input().split())
maze=[input() for _ in range(r)]
d=[[INF for i in range(r)] for _ in range(c)]
sx,sy=1,1
gx,gy=r,c
cnt=0
for i in range(r):
  for j in range(c):
    if maze[i][j]=='.':
      cnt+=1

sx-=1
sy-=1
gx-=1
gy-=1
q=queue.Queue()
dx=[-1,0,1,0]
dy=[0,-1,0,1]
q.put((sx,sy))
d[sy][sx]=0

while not q.empty():
  x,y=q.get()
  if (x,y)==(gx,gy):break
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<c and 0<=ny<r:
      if maze[ny][nx]=='.' and d[nx][ny]==INF:
        q.put((nx,ny))
        d[nx][ny]=d[x][y]+1
if d[gy][gx]==INF:
  print(-1)
else:print(cnt-d[gy][gx]-1)