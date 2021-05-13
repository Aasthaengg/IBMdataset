N = int(input())
from heapq import heapify, heappush, heappop

inf = float("inf")
def dijkstra(graph, start):  # graphは隣接リスト(繋がっている先, コスト)
    vsize = len(graph)
    dist = [inf] * vsize
    seen = [False] * vsize
    prev = [None] * vsize
    pq = []
    heapify(pq)

    dist[start] = 0
    heappush(pq, (0, start))  # heapではtuple[0]で比較されるのでこの順番で追加する
    while pq:
        cost, u = heappop(pq)
        seen[u] = True
        if dist[u] < cost:
            continue
        for v, w in graph[u]:
            temp_cost = dist[u] + w
            if not seen[v] and temp_cost < dist[v]:
                dist[v] = temp_cost
                prev[v] = u
                heappush(pq, (dist[v], v))
    return dist
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))
Q, K = map(int, input().split())
shortest_path_K = dijkstra(graph, K-1)
for _ in range(Q):
    x, y = map(int, input().split())
    print(shortest_path_K[x-1]+shortest_path_K[y-1])
