n,m,l = map(int,input().split())
abe = [list(map(int,input().split())) for i in range(m)]
dist = [[10**18 for i in range(n)] for i in range(n)]
for a,b,e in abe:
  dist[a-1][b-1] = e
  dist[b-1][a-1] = e
for k in range(n):
  for i in range(n):
    for j in range(n):
      dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
for i in range(n):
  for j in range(n):
    if dist[i][j] <= l:
      dist[i][j] = 1
    else:
      dist[i][j] = 10**18
for k in range(n):
  for i in range(n):
    for j in range(n):
      dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
q = int(input())
for i in range(q):
  s,t = map(int,input().split())
  x = dist[s-1][t-1]-1
  if x == 10**18-1:
    print(-1)
  else:
    print(x)