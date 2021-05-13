import heapq


def dijkstra(start, n_nodes, edges):
    dist = [float("inf")] * n_nodes
    dist[start] = 0
    q = [(dist[start], start)]
    heapq.heapify(q)

    while q:
        d, i = heapq.heappop(q)
        if d > dist[i]:
            continue

        for w, j in edges[i]:
            if d + w < dist[j]:
                dist[j] = d + w
                heapq.heappush(q, (dist[j], j))

    return dist


def main():
    N = int(input())
    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        edges[a].append((c, b))
        edges[b].append((c, a))

    Q, K = map(int, input().split())
    K -= 1
    query = []
    for _ in range(Q):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        query.append((x, y))
    dist = dijkstra(K, N, edges)
    for x, y in query:
        ans = dist[x] + dist[y]
        print(ans)


main()
