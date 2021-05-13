N, M = map(int, input().split())
l = []
for _ in range(M):
    a,b = list(map(int, input().split()))
    l.append([a-1,b-1])
visit = [0]*N
graph = [0]*N*N
g = []
def dfs(v):
  visit[v] = 1
  for v2 in range(N):
    if graph[v*N+v2] == 1 and visit[v2] == 0:
      g.append(v2)
    if v2 == N-1 and len(g) != 0:
      a = g[0]
      g.pop(0)
      return dfs(a)
ans = 0
for a,b in l:
  graph[a*N+b] = graph[b*N+a] = 1
for a,b, in l:
  graph[a*N+b] = graph[b*N+a] = 0
  visit = [0]*N
  dfs(0)
  if sum(visit) != N:
    ans += 1
  graph[a*N+b] = graph[b*N+a] = 1
print(ans)
