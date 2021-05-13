import heapq
N,M = map(int,input().split())
INF = float("inf")
edge = [[] for _ in range(N)]
#print(load)
#dis = [[] for _ in range(N)]
List = [] #0は未使用、1は使用
for i in range(M):
  a,b,c = map(int,input().split())
  a-=1;b-=1
  edge[a].append([c,b,i])
  edge[b].append([c,a,i])
  List.append([c,a,b,i])

def dijkstra_heap(s):
  d = [INF for _ in range(N)]
  used = [True for _ in range(N)]
  d[s] = 0
  used[s] = False
  edgelist=[]
  for e in edge[s]:
    heapq.heappush(edgelist,e)
  while len(edgelist):
    minedge = heapq.heappop(edgelist)
    if not used[minedge[1]]: #すでに探索済みの場合にはスキップ
      continue
    v = minedge[1]
    d[v] = minedge[0]
    #L.add(minedge[2]) #この道を使用したと記録
    used[v] = False
    for e in edge[v]:
      if used[e[1]]:
        heapq.heappush(edgelist,[e[0]+d[v],e[1],e[2]])
  return d

L = set([])
for i in range(N):
  dist = dijkstra_heap(i)
  for c, s, g, ID in List: #道のリストの一つ一つの点を見て、それが最短距離で使われているか確認
    if dist[s] + c == dist[g]:
      L.add(ID)
ans = M -len(L)
print(ans)