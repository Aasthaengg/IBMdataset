from collections import defaultdict
  
n,m = map(int, input().split())
abc = [list(map(int, input().split())) for i in range(m)]
INF = 10 ** 18
d = [[INF] * n for i in range(n)]
for i in range(n):
  d[i][i] = 0
road = defaultdict(int)
for a,b,c in abc:
  a -= 1
  b -= 1
  road[(a, b)] = 1
  d[a][b] = c
  d[b][a] = c

for k in range(n):
  for i in range(n):
    for j in range(n):
      if d[i][k] + d[k][j] < d[i][j]:
        d[i][j] = d[i][k] + d[k][j]
        road[(i,j)] = 0
        road[(j,i)] = 0
ans = m - sum(road.values())
print(ans)