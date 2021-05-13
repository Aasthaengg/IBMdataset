from numpy import *
from scipy.sparse.csgraph import *
N,M = map(int,input().split())
E = [list(map(int,input().split())) for m in range(M)]
G1 = zeros((N,N))
ans = 0

for a,b in E:
  G1[a-1][b-1]+=1
  G1[b-1][a-1]+=1

for a,b in E:
  G2 = G1.copy()
  G2[a-1][b-1]-=1
  G2[b-1][a-1]-=1
  D = floyd_warshall(G2)
  if inf in D:
    ans+=1

print(ans)