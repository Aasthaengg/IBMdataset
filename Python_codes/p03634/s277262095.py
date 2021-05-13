N=int(input())

import heapq
def dijkstra_heap(s):
  #始点sから各頂点への最短距離
  #indexが1～Nの場合はNの代わりにN+1
  size_v=N+1
  dist=[float("inf")]*size_v
  used=[False]*size_v
  dist[s]=0
  used[s]=True

  hq_edge=[]
  for v,w in edge[s]:
    heapq.heappush(hq_edge,(w,v))

  while len(hq_edge):
    min_w,min_v=heapq.heappop(hq_edge)
    #まだ使われてない頂点の中から最小の距離のものを探す
    if used[min_v]:
      continue

    dist[min_v]=min_w
    used[min_v]=True
    for v,w in edge[min_v]:
      if not used[v]:
        heapq.heappush(hq_edge,(min_w+w,v))

  return dist

edge=[[] for _ in range(N+1)]
for _ in range(N-1):
  a,b,c=map(int,input().split())
  edge[a].append((b,c))
  edge[b].append((a,c))
#print(edge)

Q,K=map(int,input().split())

dist=dijkstra_heap(K)
#print(dist)

for _ in range(Q):
  x,y=map(int,input().split())
  print(dist[x]+dist[y])