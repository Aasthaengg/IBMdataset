import queue
h,w=map(int,input().split())
s=[input() for _ in range(h)]
INF=10**18
dx=[-1,0,1,0]
dy=[0,-1,0,1]
ans=0
for i in range(h):
  for j in range(w):
    if s[i][j]=='#':continue
    d=[[INF]*w for _ in range(h)]
    d[i][j]=0
    q=queue.Queue()
    q.put((i,j))
    while not q.empty():
      x,y=q.get()
      for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<h and 0<=ny<w:
          if s[nx][ny]=='.' and d[nx][ny]==INF:
            q.put((nx,ny))
            d[nx][ny]=d[x][y]+1
            ans=max(ans,d[nx][ny])
print(ans)
