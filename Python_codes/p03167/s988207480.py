import queue
INF=10**8
R=10**9+7
h,w=map(int,input().split())
maze=[input() for _ in range(h)]
d=[[0 for i in range(h)] for _ in range(w)]
sx=0
sy=0
gx=w-1
gy=h-1
q=queue.Queue()
dx=[1,0]
dy=[0,1]
q.put((sx,sy))
d[sy][sx]=1
while not q.empty():
  x,y=q.get()
  if (x,y)==(gx,gy):break
  for i in range(2):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<w and ny<h:
      if maze[ny][nx]=='.':
        if d[nx][ny]==0:
          q.put((nx,ny))
          d[nx][ny]=d[x][y]
        else:d[nx][ny]+=d[x][y]
print(d[gx][gy]%R)