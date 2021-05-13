from heapq import heapify, heappush, heappop

inf = float("inf")
def dijkstra(start):  # graphは隣接リスト(繋がっている先, コスト)
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
    return dist, prev
N, M, R = map(int, input().split())
rlist = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A-1].append((B-1, C))
    graph[B-1].append((A-1, C))
shortest_path = [dijkstra(i) for i in range(N)]
from itertools import permutations
ans = 10**9

for path in permutations(rlist):
    cost = 0
    for i in range(R-1):
        cost += shortest_path[path[i]-1][0][path[i+1]-1]
    ans = min(ans, cost)
print(ans)