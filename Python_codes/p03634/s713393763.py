n=int(input())
edge=[[]for _ in range(n)]
for _ in range(n-1):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  edge[a].append((b,c))
  edge[b].append((a,c))
from heapq import heappop,heappush
def dijkstra(s,n,edge):
  inf=10**20
  ans=[inf]*n
  ans[s]=0
  root=[-1]*n
  h=[[0,s]]
  while h:
    c,v=heappop(h)
    if ans[v]<c:continue
    for u,t in edge[v]:
      if c+t<ans[u]:
        ans[u]=c+t
        root[u]=v
        heappush(h,[c+t,u])
  return ans
q,k=map(int,input().split())
xy=[list(map(int,input().split()))for _ in range(q)]
d=dijkstra(k-1,n,edge)
for x,y in xy:
  print(d[x-1]+d[y-1])