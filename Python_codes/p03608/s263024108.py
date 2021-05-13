n, m, r = map(int, input().split())
R = list(map(int, input().split()))
R = [x-1 for x in R]

def warshal_floyd(d):
  for k in range(n):
    for i in range(n):
      for j in range(n):
        d[i][j] = min(d[i][j], d[i][k]+d[k][j])
  return d

d = [[float('inf') for i in range(n)] for j in range(n)]

for i in range(m):
    a,b,c = map(int, input().split())
    a, b = a-1, b-1
    d[a][b] = c
    d[b][a] = c

for i in range(n):
    d[i][i] = 0

d = warshal_floyd(d)
import itertools
ans = float('inf')
for p in itertools.permutations(R):
    temp = 0
    for i in range(r-1):
        temp += d[p[i]][p[i+1]]
    ans = min(temp, ans)
print(ans)
