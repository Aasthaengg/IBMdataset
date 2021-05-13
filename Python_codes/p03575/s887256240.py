def dfs_traverse(adj, visited, u=0):
  visited[u] = True
  for v in adj[u]:
    if not visited[v]:
      dfs_traverse(adj, visited, v)


def calc_num_of_bridges(edges, adj):
  n = len(adj)
  bridge_cnt = 0
  for a, b in edges:
    adj[a].remove(b)
    adj[b].remove(a)
    # check
    visited = [False] * n
    dfs_traverse(adj, visited)
    if not all(visited):
      bridge_cnt += 1
    # restore
    adj[a].append(b)
    adj[b].append(a)
  return bridge_cnt


n, m = map(int, input().split())
adj = [[] for _ in range(n)]
edges = []
for _ in range(m):
  a, b = map(lambda x: int(x)-1, input().split())
  edges.append((a, b))
  adj[a].append(b)
  adj[b].append(a)

print(calc_num_of_bridges(edges, adj))
