n,m=map(int,input().split())
def BellmanFord(edges,num_v,s):
  #グラフの初期化
  inf=float("inf")
  dist=[inf]*num_v
  dist[s]=0
  
  #辺の緩和
  for i in range(num_v-1):
    for edge in edges: #edges[頂点][頂点][重み]
      if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
  ans=-dist[n-1]
  neg=[False]*num_v
  for i in range(num_v):
    for edge in edges: #edges[頂点][頂点][重み]
      if dist[edge[1]] > dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
        neg[edge[1]]=True
      if neg[edge[0]]:
        neg[edge[1]]=True
  if neg[n-1]:
    ans='inf'
  return ans
edges=[]
for i in range(m):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  c*=-1
  edges.append((a,b,c))
print(BellmanFord(edges,n,0))