n,m,l = map(int, input().split())
INF = 1001001001
dist = [[INF for i in range(n)] for i in range(n)]
#make graph
for i in range(n):
  dist[i][i] = 0
for i in range(m):
  a, b, c = map(int, input().split())
  dist[a-1][b-1] = dist[b-1][a-1] = c
#warshall-froyd
for k in range(n):
  for i in range(n):
    for j in range(n):
      dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
dist2 =  [[INF for i in range(n)] for i in range(n)]
for i in range(n):
  for j in range(n):
    if dist[i][j] <=l:
      dist2[i][j] = 1
#warshall-froyd
for k in range(n):
  for i in range(n):
    for j in range(n):
      dist2[i][j] = min(dist2[i][j], dist2[i][k]+dist2[k][j])
q = int(input())
for i in range(q):
  s,t = map(int, input().split())
  if dist2[s-1][t-1] == INF:
    print(-1)
  else:
    print(dist2[s-1][t-1]-1)