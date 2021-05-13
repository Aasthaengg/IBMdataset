N,M = map(int,input().split())
ABC = []
for i in range(M):
  a,b,c=map(int,input().split())
  c=-c
  ABC.append([a,b,c])

def BellmanFord():
  inf=float("Inf")
  dist=[inf for i in range(N)]
  dist[0]=0
  
  for i in range(N):
    for edge in ABC:
      if dist[edge[1]-1] > dist[edge[0]-1] + edge[2]:
        dist[edge[1]-1] = dist[edge[0]-1] + edge[2]
        if i==N-1 and edge[1]-1==N-1: return inf
    
  return -dist[N-1]
  
print(BellmanFord())