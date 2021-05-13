import sys
readline = sys.stdin.readline

N,M,R = map(int,readline().split())
r = list(map(int,readline().split()))
INF = 10 ** 10

G = [[INF] * N for i in range(N)]
for i in range(M):
  a,b,c = map(int,readline().split())
  G[a - 1][b - 1] = c
  G[b - 1][a - 1] = c
  
for i in range(N):
  G[i][i] = 0
  
for k in range(N):
  for i in range(N):
    for j in range(N):
      G[i][j] = min(G[i][j], G[i][k] + G[k][j])
      
import itertools
ans = INF
for perm in itertools.permutations(range(R)):
  dist = 0
  for i in range(1, len(perm)):
    dist += G[r[perm[i - 1]] - 1][r[perm[i]] - 1]
  if ans > dist:
    ans = dist
    
print(ans)
