import copy

N = int(input())
graph = []
road = []
for _ in range(N):
  A = list(map(int, input().split()))
  graph.append(A)
  road.append(copy.deepcopy(A))

exist = 1
for k in range(N):
  for i in range(N):
    for j in range(N):
      if graph[i][j] > graph[i][k] + graph[k][j]:
        exist = 0
        break
      if graph[i][j] != 0 and graph[i][k] != 0 and graph[k][j] != 0:
        if graph[i][j] == graph[i][k] + graph[k][j]:
          road[i][j] = 0
    if exist == 0:
      break
  if exist == 0:
    break

if exist == 0:
  print(-1)
else:
  ans = 0
  for row in road:
    ans += sum(row)
  print(ans//2)