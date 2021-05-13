N,M,P = map(int,input().split())
E = []
for i in range(M):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  c=-c+P
  E.append([a,b,c])
  
def BellmanFord(s,g):
  #グラフの初期化
  inf=float("inf")
  dist=[inf for i in range(N)]
  dist[s]=0
  rout=[]
  
  #辺の緩和
  for i in range(N):
    for edge in E:
      if dist[edge[1]] > dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
        if i==N-1: dist[edge[1]]=-inf
  for i in range(N):
    for edge in E:
      if dist[edge[1]] > dist[edge[0]] + edge[2]:
        dist[edge[1]] = dist[edge[0]] + edge[2]
  if dist[g] == -inf:return -1
  return max(0,-dist[g])
print(BellmanFord(0,N-1))