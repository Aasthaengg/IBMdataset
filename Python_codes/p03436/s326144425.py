from collections import deque
def MI(): return map(int, input().split())
INF=float('inf')
def bfs():
  que=deque()
  que.append((sx,sy))
  dist=[[INF] *W for _ in range(H)]
  dist[sx][sy]=0
  dx=[1,0,-1,0]
  dy=[0,1,0,-1]
  while que:
    x,y=que.popleft()
    if x==gx and y==gy:
      break
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<H and 0<=ny<W:
        if Map[nx][ny]!='#':
          if dist[nx][ny]==INF:
            dist[nx][ny]=dist[x][y]+1
            que.append((nx,ny))
  return dist[gx][gy]
H,W=MI()
Map=[list(input()) for i in range(H)]
sx,sy=0,0
gx,gy=H-1,W-1
white=0
for i in range(H):
  for j in range(W):
    if Map[i][j]=='.':
      white+=1
res=bfs()
if 0<res<INF:
  print(white-res-1)
else:
  print(-1)