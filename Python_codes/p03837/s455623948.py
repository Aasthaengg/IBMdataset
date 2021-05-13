N,M=map(int,input().split())

def warshall_floyd(d):
  #d[i][j]: iからjへの最短距離
  for k in range(size_v):
    for i in range(size_v):
      for j in range(size_v):
        d[i][j]=min(d[i][j],d[i][k]+d[k][j])
  return d

abclist=[]
for i in range(M):
  a,b,c=map(int,input().split())
  abclist.append((a,b,c))
#print(graph)

size_v=N+1
dist=[[float("inf")]*size_v for i in range(size_v)] 

for a,b,c in abclist:
  dist[a][b]=c
  dist[b][a]=c
for i in range(size_v):
  dist[i][i]=0

dist=warshall_floyd(dist)
#print(dist)
  
answer_set=set()
for a,b,c in abclist:
  if dist[a][b]==c:
    answer_set.add((a,b,c))
    
print(M-len(answer_set))