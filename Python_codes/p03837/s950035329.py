n,m = map(int,input().split())
edge = [tuple(map(int,input().split())) for _ in range(m)]
g = [[10**8]*(n) for i in range(n)]
for i in range(n):
  g[i][i] = 0
for a,b,c in edge:
  g[a-1][b-1] = c
  g[b-1][a-1] = c

for k in range(n):
  for i in range(n-1):
    for j in range(i+1,n):
      if g[i][j] > g[i][k] + g[k][j]:
        g[i][j] = g[i][k] + g[k][j]
        g[j][i] = g[i][j]

ans = 0
for a,b,c in edge:
  a -= 1; b -= 1
  if a > b:
    a,b = b,a
  for i in range(n):
    if abs(g[i][a]-g[i][b]) == c:
      break
  else:
    ans += 1
print(ans)