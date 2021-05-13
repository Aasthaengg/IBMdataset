N,M=map(int,input().split())

import heapq
def dijkstra_heap(s):
  #始点sから各頂点への最短距離
  dist=[float("inf")]*size_v  
  used=[False]*size_v
  dist[s]=0
  used[s]=True

  hq_edge=[]
  for v,w,i in graph[s]:
    heapq.heappush(hq_edge,(w,v,i))

  while hq_edge:
    min_w,min_v,ei=heapq.heappop(hq_edge)
    if dist[min_v]>=min_w:
      answer_set.add(ei)
    #まだ使われてない頂点の中から最小の距離のものを探す
    if used[min_v]:
      continue

    dist[min_v]=min_w
    used[min_v]=True
    for v,w,ei2 in graph[min_v]:
      if not used[v]:
        heapq.heappush(hq_edge,(min_w+w,v,ei2))

  return dist

graph=[[] for _ in range(N+1)]
for i in range(M):
  a,b,c=map(int,input().split())
  graph[a].append((b,c,i))
  graph[b].append((a,c,i))
#print(graph)

size_v=N+1
answer_set=set()
for i in range(1,N+1):
  dist=dijkstra_heap(i)
  #print(dist)
    
#print(sorted(list(answer_set)))
print(M-len(answer_set))