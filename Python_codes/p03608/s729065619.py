import itertools
N, M, R = map(int, input().split())
r = list(map(lambda x:int(x)-1, input().split()))
graph = [[] for _ in range(N)]
d = [[float('inf')]*N for _ in range(N)]
for _ in range(M):
  a, b, c = map(int, input().split())
  a -= 1
  b -= 1
  graph[a] += [[b, c]]
  graph[b] += [[c, a]]
  d[a][b] = c
  d[b][a] = c

for i in range(N):
  d[i][i] = 0

def warshall_floyd(d):
  #d[i][j]: iからjへの最短距離
  for k in range(N):
    for i in range(N):
      for j in range(N):
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