from collections import defaultdict
from copy import deepcopy


def dfs(graph, v, visited):
    visited.add(v)
    for nv in graph[v]:
        if nv not in visited:
            dfs(graph, nv, visited)
    return visited


def is_connected(graph, nodes_cnt):
    visited = dfs(graph, 1, set())
    if len(visited) == nodes_cnt:
        return True
    else:
        return False


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
G = defaultdict(set)
for u, v in edges:
    G[u].add(v)
    G[v].add(u)
ans = 0
for u, v in edges:
    H = deepcopy(G)
    H[u] -= {v}
    H[v] -= {u}
    if not is_connected(H, N):
        ans += 1
print(ans)
