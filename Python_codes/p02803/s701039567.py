h,w=map(int,input().split())
s=[]
import heapq
INF=10**9
def Dijkstra(graph, start):
  dist=[INF]*len(graph)
  parent=[INF]*len(graph)
  queue=[(0, start)]
  while queue:
    path_len, v=heapq.heappop(queue)
    if dist[v]==INF: 
      dist[v]=path_len
      for w in graph[v]:
        if dist[w[0]]==INF:
          parent[w[0]]=v
          heapq.heappush(queue, (dist[v]+w[1], w[0]))         
  return (dist,parent)
for i in range(h):
  a=input()
  s.append(a)
graph=[]
ans=0
for i in range(h):
  for j in range(w):
    graph.append([])
for i in range(h):
  for j in range(w):
    if s[i][j]=='.':
      if i>0 and s[i-1][j]=='.':
        graph[i*w+j].append([(i-1)*w+j,1])
      if i<h-1 and s[i+1][j]=='.':
        graph[i*w+j].append([(i+1)*w+j,1])
      if j>0 and s[i][j-1]=='.':
        graph[i*w+j].append([i*w+j-1,1])
      if j<w-1 and s[i][j+1]=='.':
        graph[i*w+j].append([i*w+j+1,1])
for i in range(h):
  for j in range(w):
    if s[i][j]=='.':
      a,b=Dijkstra(graph,i*w+j)
      for k in range(h):
        for l in range(w):
          if a[k*w+l]!=INF:
            ans=max(ans,a[k*w+l])
print(ans)