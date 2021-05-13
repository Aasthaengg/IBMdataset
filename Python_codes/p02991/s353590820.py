import sys
input = sys.stdin.readline
n,m=map(int,input().split())
edge=[[] for i in range(3*n)]
for i in range(m):
  u,v=map(int,input().split())
  for j in range(3):
    edge[u-1+j*n].append([1,(v-1+(j+1)*n)%(3*n)])
import heapq
def dijkstra_heap(s):
  d=[float("inf")]*(3*n)
  used=[True]*(3*n)
  d[s]=0
  used[s]=False
  edgelist=[]
  for e in edge[s]:
    heapq.heappush(edgelist,e)
  while edgelist:
    minedge = heapq.heappop(edgelist)
    if not used[minedge[1]]:
      continue
    v = minedge[1]
    d[v] = minedge[0]
    used[v] = False
    for e in edge[v]:
      if used[e[1]]:
        heapq.heappush(edgelist,[e[0]+d[v],e[1]])
  return d
s,t=map(int,input().split())
ans=dijkstra_heap(s-1)[t-1]
print(ans//3 if ans%3==0 else -1)