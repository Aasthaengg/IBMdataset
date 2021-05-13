n,m=map(int,input().split())
def BellmanFord(edges,num_v,s):
  #グラフの初期化
  inf=float("inf")
  dist=[inf]*num_v
  dist[s]=0
  
  #辺の緩和
  for i in range(num_v):
    for edge in edges: #edges[頂点][頂点][重み]
      if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
        if i==num_v-1 and edge[1]==num_v-1: return -1
  
  return dist[num_v-1]
edges=[]
for i in range(m):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  c*=-1
  edges.append((a,b,c))
if BellmanFord(edges,n,0)==-1:
  print('inf')
else:
  print(-BellmanFord(edges,n,0))