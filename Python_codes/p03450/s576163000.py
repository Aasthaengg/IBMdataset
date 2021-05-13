N, M = map(int, input().split())
LRD = [list(map(int, input().split())) for _ in range(M)]

INF = 10 ** 10
dist = [INF] * (N + 1)

graph = [[] for _ in range(N + 1)]
for i in range(M):
  L, R, D = LRD[i]
  graph[L].append((R, D))
  graph[R].append((L, -D))
#print("graph:", graph)

for i in range(1, N + 1):
  if dist[i] == INF:
    stack = [i]
    dist[i] = 0
    max_d = 0
    min_d = 0
    
    while stack:
      l = stack.pop()
      for r, d in graph[l]:
        if dist[r] != INF:
          if dist[r] != dist[l] + d:
            print("No")
            exit()
          else:
            continue
        else:
          stack.append(r)
          dist[r] = dist[l] + d
#print("dist:", dist)
print("Yes")       