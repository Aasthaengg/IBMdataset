import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edge = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    edge[a].append((b, c, i+1))
    edge[b].append((a, c, i+1))

used = [False] * (M + 1)


def dijkstra(start):
    inf = 10**18
    dist = [inf] * (N + 1)
    visited = [False] * (N + 1)
    dist[start] = 0
    visited[start] = False
    node = [(0, start, 0)]
    while node:
        d, s, e = heapq.heappop(node)
        if dist[s] < d:
            continue
        used[e] = True

        for t, cost, ind in edge[s]:
            if dist[t] > d + cost:
                dist[t] = d + cost
                heapq.heappush(node, (d + cost, t, ind))
    return


for i in range(1, N + 1):
    dijkstra(i)

ans = used.count(False)
print(ans)

