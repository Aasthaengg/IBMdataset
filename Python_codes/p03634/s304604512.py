# D - Transit Tree Path
# https://atcoder.jp/contests/abc070/tasks/abc070_d

from heapq import heappop, heappush

INF = float("inf")

def dijkstra(n, G, s):
    dist = [INF] * n
    dist[s] = 0
    hq = [(0, s)]
    while hq:
        d, v = heappop(hq)
        if dist[v] < d:
            continue
        for child, child_d in G[v]:
            if dist[child] > dist[v] + child_d:
                dist[child] = dist[v] + child_d
                heappush(hq, (dist[child], child))
    return dist

n = int(input())
edge = [list(map(int, input().split())) for _ in range(n - 1)]
graph = [[] for _ in range(n)]

for a, b, c in edge:
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

q, k = map(int, input().split())

d = dijkstra(n, graph, k - 1)

for _ in range(q):
  x, y = map(int, input().split())
  ans = d[x - 1] + d[y - 1]
  print(ans)
