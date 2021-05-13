from itertools import permutations
N, M, R, *L = map(int, open(0).read().split())
city = L[:R]
inf = L[R:]
dist = [[10**10]*N for i in range(N)]
for x,y,c in zip(*[iter(inf)]*3):
  dist[x-1][y-1] = c
  dist[y-1][x-1] = c
for i in range(N):
  dist[i][i] = 0

for k in range(N):
  for i in range(N):
    for j in range(N):
      dist[i][j] = min(dist[i][k]+dist[k][j], dist[i][j])

ans = 10**10
for m in permutations(city):
  n = 0
  for i in range(R-1):
    n += dist[m[i]-1][m[i+1]-1]
  ans = min(ans,n)
print(ans)  
  
