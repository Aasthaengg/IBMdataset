N, M = map(int, input().split())
G = [[] for i in range(3 * N)]
for i in range(M):
    u, v = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append([v + N, 1])
    G[u + N].append([v + 2 * N, 1])
    G[u + 2 * N].append([v, 1])

S, T = map(int, input().split())
S, T = S - 1, T - 1


def dijkstra(graph, start, inf=float('inf')):
    import heapq
    n = len(graph)
    distances = [inf] * n
    distances[start] = 0
    visited = [False] * n

    # 距離・頂点
    hq = [(0, start)]
    while hq:
        dist, fr = heapq.heappop(hq)
        visited[fr] = True

        for to, cost in graph[fr]:
            new_dist = distances[fr] + cost
            if (visited[to]) or (distances[to] <= new_dist):
                continue

            distances[to] = new_dist
            heapq.heappush(hq, (new_dist, to))

    return distances


distances = dijkstra(G, S)
print(distances[T] // 3 if distances[T] != float('inf') else -1)
