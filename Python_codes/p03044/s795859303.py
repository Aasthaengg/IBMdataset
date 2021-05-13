import sys
sys.setrecursionlimit(100000)

N = int(input())
adj_list = { i: [] for i in range(N+1) }
for _ in range(N-1):
  u,v,w = map(int, input().split())
  adj_list[u].append([v,w])
  adj_list[v].append([u,w])

res = [None] * N
visited = [False] * (N+1)
def dfs(node, c, w):
  res[node-1] = c
  visited[node] = True

  for nei, nw, in adj_list[node]:
    if not visited[nei]:
      if (w+nw)%2 == 0:
        dfs(nei, 0, w+nw)
      else:
        dfs(nei, 1, w+nw)

dfs(1, 0, 0)
for r in res: print(r)