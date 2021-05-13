import sys
input = sys.stdin.readline
N, M = map(int, input().split())
e = [set() for _ in range(N + 1)]
reve = [[] for _ in range(N + 1)]
for _ in range(M):
  u, v, c = map(int, input().split())
  e[u].add((v, -c))
  reve[v].append(u)

vis = [0] * (N + 1)
def revdfs(x):
  global vis
  if x == 1: return True
  res = 0
  for y in reve[x]:
    if vis[y]: continue
    vis[y] = 1
    res |= revdfs(y)
  return res
def dfs(x):
  global vis
  if x == N: return True
  res = 0
  for y, _ in e[x]:
    if vis[y]: continue
    vis[y] = 1
    res |= dfs(y)
  return res
banned = [0] * (N + 1)
for x in range(1, N + 1):
  vis = [0] * (N + 1)
  banned[x] |= revdfs(x) ^ 1
  vis = [0] * (N + 1)
  banned[x] |= dfs(x) ^ 1

for x in range(1, N + 1):
  t = list(e[x])
  for y, d in t:
    if banned[x] | banned[y]: e[x].discard((y, d))
#print(banned)
INF = 10**18
dist = [INF] * (N + 1)
dist[1] = 0
update = 1
for _ in range(N + 1):
    update = 0
    for v, x in enumerate(e):
        for t, cost in x:
            if dist[v] != INF and dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                update = 1
    if not update:
        break
else:
  print("inf")
  exit(0)
print(-dist[N])