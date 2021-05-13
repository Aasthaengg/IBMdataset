from collections import deque


def bellman_ford(start: int, graph: list) -> list:
    """bellman-ford法: 始点startから各頂点への最短距離を求める(負辺OK)
    計算量: O(|E||V|)
    """
    INF = float("inf")
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    if n == 1:
        return False, [0]
    for _ in range(n):
        update = False
        for v, edge in enumerate(graph):
            for nxt_v, cost in edge:
                if (not reach[nxt_v]) or (not rev_reach[nxt_v]):
                    continue
                if dist[v] != INF and dist[nxt_v] > dist[v] + cost:
                    dist[nxt_v] = dist[v] + cost
                    update = True
        if not update:
            return dist[n - 1]
    return -INF


n, m, p = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]

graph = [[] for i in range(n)]
rev_graph = [[] for i in range(n)]
for a, b, cost in info:
    a -= 1
    b -= 1
    graph[a].append((b, -(cost - p)))
    rev_graph[b].append(a)

reach = [False] * n
reach[0] = True
q = deque([0])
while q:
    v = q.popleft()
    for nxt_v, _ in graph[v]:
        if reach[nxt_v]:
            continue
        reach[nxt_v] = True
        q.append(nxt_v)
        
rev_reach = [False] * n
rev_reach[n - 1] = True
q = deque([n - 1])
while q:
    v = q.popleft()
    for nxt_v in rev_graph[v]:
        if rev_reach[nxt_v]:
            continue
        rev_reach[nxt_v] = True
        q.append(nxt_v)

dist = bellman_ford(0, graph)
if dist == -float("inf"):
    print(-1)
else:
    print(max(-dist, 0))
