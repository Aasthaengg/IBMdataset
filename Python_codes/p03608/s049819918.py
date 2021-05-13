import heapq
import itertools
n, m, r = map(int, input().split())
r = list(map(lambda x:int(x)-1, input().split()))
d = [[float('inf')]*n for _ in range(n)]
for _ in range(m):
  a, b, t = map(int, input().split())
  a -= 1
  b -= 1
  d[a][b] = t
  d[b][a] = t
for i in range(n):
  d[i][i] = 0

def warshall_floyd(d):
  #d[i][j]: iからjへの最短距離
  for k in range(n):
    for i in range(n):
      for j in range(n):
        d[i][j] = min(d[i][j],d[i][k] + d[k][j])
  return d  

d = warshall_floyd(d)
ans = float('inf')
for v in itertools.permutations(r):
  tmp = 0
  for i in range(len(v)-1):
    tmp += d[v[i]][v[i+1]]
  ans = min(ans, tmp)

print(ans)
