n,m,l = map(int,input().split())
inf = 10 ** 18
d1 = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
  d1[i][i] = 0
for _ in range(m):
  a,b,c = map(int,input().split())
  a -= 1
  b -= 1
  d1[a][b] = c
  d1[b][a] = c
for k in range(n):
  for i in range(n):
    for j in range(n):
      d1[i][j] = min(d1[i][j], d1[i][k]+d1[k][j])
d2 = [[inf for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if d1[i][j] == 0:
      d2[i][j] = 0
    elif d1[i][j] <= l:
      d2[i][j] = 1
for k in range(n):
  for i in range(n):
    for j in range(n):
      d2[i][j] = min(d2[i][j], d2[i][k]+d2[k][j])
q = int(input())
for _ in range(q):
  s,t = map(int,input().split())
  s -= 1
  t -= 1
  ans = d2[s][t]
  if ans >= inf:
    print(-1)
  else:
    print(ans-1)