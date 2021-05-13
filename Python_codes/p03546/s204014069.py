h,w = map(int,input().split())
dist = [[float("inf")] * 10 for _ in range(10)]
for i in range(10):
  cost = list(map(int,input().split()))
  for j in range(10):
    dist[i][j] = cost[j]
wall = []
for _ in range(h):
  wall.append(list(map(int,input().split())))
V = 10
for k in range(V):
  for i in range(V):
    for j in range(V):
      if dist[i][k]!=float("inf") and dist[k][j]!=float("inf"):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
ans = 0
for wa in wall:
  for wi in wa:
    if wi != -1:
      ans += dist[wi][1]
print(ans)

