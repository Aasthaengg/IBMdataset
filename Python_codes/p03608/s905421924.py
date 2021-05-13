import itertools
N,M,R=map(int,input().split())
rlist=list(map(int,input().split()))

def warshall_floyd(d):
  #d[i][j]: iからjへの最短距離
  for k in range(N+1):
    for i in range(N+1):
      for j in range(N+1):
        d[i][j]=min(d[i][j],d[i][k]+d[k][j])
  return d

# vlistに点のリスト、dist[vi][vj]に辺(vi,vj)のコストを入れて呼び出す
dist=[[float("inf")]*(N+1) for i in range(N+1)] 
for i in range(M):
  a,b,c=map(int,input().split())
  dist[a][b]=c
  dist[b][a]=c
for i in range(N+1):
  dist[i][i]=0

dist=warshall_floyd(dist)
#print(dist)

max_answer=float("inf")
for perm in itertools.permutations(rlist):
  #print(perm)
  answer=0
  for i in range(R-1):
    answer+=dist[perm[i]][perm[i+1]]
  
  max_answer=min(max_answer,answer)  
  
print(max_answer)