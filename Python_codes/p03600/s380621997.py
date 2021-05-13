import sys
N=int(input())

def warshall_floyd(d):
  #d[i][j]: iからjへの最短距離
  for k in range(N):
    for i in range(N):
      for j in range(N):
        if i<j and i!=k and k!=j and d[i][j]==d[i][k]+d[k][j]:
          #print((i,k),(k,j))
          shortcut_set.add((i,j))
        d[i][j]=min(d[i][j],d[i][k]+d[k][j])
  return d

mat=[]
for i in range(N):
  mat.append([int(x) for x in input().split()])
#print(mat)

dist=[[float("inf")]*N for i in range(N)]
graph=[[] for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i==j:
      dist[i][i]=0
    else:
      graph[i].append((j,mat[i][j]))
      dist[i][j]=mat[i][j]
#print(graph)
#print(dist)

shortcut_set=set()
dist=warshall_floyd(dist)
#print(dist)

for i in range(N):
  for j in range(N):
    if dist[i][j]!=mat[i][j]:
      print(-1)
      sys.exit(0)
      
answer=0
for i in range(N):
  for j in range(i+1,N):
    if not (i,j) in shortcut_set:
      answer+=dist[i][j]
      
print(answer)