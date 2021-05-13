from collections import deque
def MI(): return map(int, input().split())
def bfs():
  dist=[[INF] * (W+1) for _ in range(H+1)]
  dist[sx][sy]=0
  que=deque([])
  que.append((sx,sy))
  di=(-1,0,1,0)
  dj=(0,-1,0,1)
  while que:
    (x,y)=que.popleft()
    if x==gx and y==gy:
      break
    for k in range(4):
      ni=x+di[k]
      nj=y+dj[k]
      if 0<=ni<H and 0<=nj<W:
        if Map[ni][nj]!='#':
          if dist[ni][nj]==INF:
            dist[ni][nj]=dist[x][y]+1
            que.append((ni,nj))
  return dist[gx][gy]
H,W=MI()
Map=[list(input()) for _ in range(H)]
#Map2=[[input()] for _ in range(H)]
INF=float('inf')
(sx,sy)=(0,0)
(gx,gy)=(H-1,W-1)
res=bfs()
white=0
for i in range(H):
  for j in range(W):
    if Map[i][j]=='.':
      white+=1
if 0<res<INF:
  ans=white-res-1
  print(ans)
else:
  print(-1)