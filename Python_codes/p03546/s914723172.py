INF = 10 ** 20
H, W = map(int, input().split())
power = 0
graph = []
for i in range(10):
  graph.append(list(map(int, input().split())))

for k in range(10):
  for i in range(10):
    for j in range(10):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
  
for h in range(H):
  A = list(map(int, input().split()))
  for w in range(W):
    if A[w] == -1:
      continue
    else:
      power += graph[A[w]][1]

print(power)