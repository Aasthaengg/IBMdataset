h,w=map(int,input().split())
a=[input() for _ in range(h)]
visited=[[0]*w for _ in range(h)]
from collections import deque
q=deque([])
for i in range(h):
  for j in range(w):
    if a[i][j]=="#":
      q.append((i,j,0))
      visited[i][j]=1
ans=0
while q:
  i,j,count=q.popleft()
  ans=max(ans,count)
  for nxi,nxj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
    if 0<=nxi<h and 0<=nxj<w and visited[nxi][nxj]==0:
      visited[nxi][nxj]=1
      q.append((nxi,nxj,count+1))
print(ans)
