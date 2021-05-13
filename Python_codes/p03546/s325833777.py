n,m = map(int,input().split())
dist = [list(map(int,input().split())) for i in range(10)]
dist.append([0]*10)
for k in range(10):
  for i in range(10):
    for j in range(10):
      dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = 0
for i in range(n):
  a = list(map(int,input().split()))
  for j in a:
    ans += dist[j][1]
print(ans)