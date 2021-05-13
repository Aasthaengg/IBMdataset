from itertools import permutations
N, M, R = map(int, input().split())
r = [int(c)-1 for c in input().split()]
cost = [[float('inf')]*N for i in range(N)]
for i in range(M):
  a, b, c = map(int, input().split())
  cost[a-1][b-1] = c
  cost[b-1][a-1] = c
def warshall_floyd(d,n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d
dist = warshall_floyd(cost,N)
ls = list(permutations(r))
ans = -1
for l in ls:
  m = 0
  p = l[0]
  flag = False
  for q in l[1:]:
    m += dist[p][q]
    p = q
  if ans==-1 or ans>m:
    ans = m
print(ans)