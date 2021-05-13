from collections import deque
def MI(): return map(int, input().split())

def bfs(field,s):
  MOVE=[(0,1),(1,0),(0,-1),(-1,0)]
  q=deque([(0,s)])
  dist=[[-1]*W for _ in range(H)]
  #d,i,j=-1,-1,-1
  while q:
    d,(i,j)=q.popleft()
    if dist[i][j]!=-1:
      continue
    dist[i][j]=d
    for di,dj in MOVE:
      ni,nj=i+di,j+dj
      if not 0<=ni<H or not 0<=nj<W:
        continue
      if dist[ni][nj]!=-1:
        continue
      if field[ni][nj]=='#':
        continue
      q.append((d+1,(ni,nj)))
  return d
ans=0
H,W=MI()
field=[input() for _ in range(H)]
for i in range(H):
  for j in range(W):
    if field[i][j]=='.':
      d=bfs(field,(i,j))
      ans=max(ans,d)
print(ans)