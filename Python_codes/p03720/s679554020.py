
N, M = map(int, input().split())
graph = [0]*N
for _ in range(M):
  a, b = map(lambda x:int(x)-1, input().split())
  graph[a] += 1
  graph[b] += 1
for i in range(N):
  print(graph[i])