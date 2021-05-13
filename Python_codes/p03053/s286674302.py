from collections import deque

h,w=map(int,input().split())
INF=float('inf')
G=[]
for _ in range(h):
  s=input()
  S=[]
  for i in range(w):
    S.append(s[i])
  G.append(S)
  
dist=[[INF for i in range(w)] for j in range(h)]
Q=deque()
for i in range(h):
  for j in range(w):
    if G[i][j]=='#':
      dist[i][j]=0
      Q.append((i,j))
while Q:
  pi,pj=Q.popleft()
  for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
    ni,nj=pi+di,pj+dj
    if 0>ni or ni>h-1:
      continue
    if 0>nj or nj>w-1:
      continue
    if G[ni][nj]=='#':
      continue
    if dist[ni][nj]>dist[pi][pj]+1:
      dist[ni][nj]=dist[pi][pj]+1
      Q.append((ni,nj))
ans=-INF
for i in range(h):
  for j in range(w):
    ans=max(ans,dist[i][j])
print(ans)