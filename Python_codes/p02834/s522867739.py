N, u, v = map(int, input().split())
u, v = u - 1, v - 1
T = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    T[a].append([b, 1])
    T[b].append([a, 1])


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


U_dist = dijkstra(T, u)
V_dist = dijkstra(T, v)

ans_candidates = [dv for du, dv in zip(U_dist, V_dist) if du < dv]
print(max(ans_candidates) - 1)
