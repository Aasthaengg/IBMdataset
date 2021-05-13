from collections import deque
h,w=map(int,input().split())
G=[]
for _ in range(h):
  s=input()
  S=[]
  for i in range(w):
    S.append(s[i])
  G.append(S)

si,sj=0,0
gi,gj=h-1,w-1
INF=float('inf')
dist=[[INF for i in range(w)] for j in range(h)]
dist[si][sj]=1
Q=deque()
Q.append((si,sj))
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
ans=0      
for i in range(h):
  for j in range(w):
    if G[i][j]=='.':
      ans+=1
ans-=dist[gi][gj]
if ans<0:
  print(-1)
else:
  print(ans)