import heapq


def dijkstra(n, s, g):
    h = [(0, s)]
    heapq.heapify(h)
    cost = [float("Inf")] * (n + 1)  # cost: i -> j
    cost[s] = 0

    while h:
        c, v = heapq.heappop(h)
        if c > cost[v]:
            continue
        for d, u in g[v]:
            d_s_u = d + cost[v]
            if d_s_u < cost[u]:
                cost[u] = d_s_u
                heapq.heappush(h, (d_s_u, u))

    return cost


def main():
    n, m, *abc = map(int, open(0).read().split())
    g = [[] for _ in range(n + 1)]

    for a, b, c in zip(*[iter(abc)] * 3):
        g[a].append([c, b])
        g[b].append([c, a])

    ans = 0
    checked = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        cost = dijkstra(n, i, g)
        for j, k in g[i]:
            if checked[i][k]:
                continue
            if j > cost[k]:
                ans += 1

            checked[i][k] = True
            checked[k][i] = True

    print(ans)


if __name__ == '__main__':
    main()
