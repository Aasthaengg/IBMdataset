def dijkstra(s, stop, g):
    import heapq

    n = len(g)
    heap = [(0, s)]
    heapq.heapify(heap)

    prev = [-1] * n
    cost = [float("Inf")] * n
    cost[s] = 0

    while heap:
        c, v = heapq.heappop(heap)
        x = cost[v]
        if c > x:
            continue
        for d, u in g[v]:
            path = d + x
            if path < cost[u]:
                cost[u] = path
                prev[u] = v
                heapq.heappush(heap, (path, u))
            if u == stop:
                break

    return prev, cost


def main():
    from collections import deque

    n, *uv = map(int, open(0).read().split())
    g = [[] for _ in range(n + 1)]

    for i, j in zip(*[iter(uv)] * 2):
        g[i].append([1, j])
        g[j].append([1, i])

    dk, cost = dijkstra(n, 1, g)
    l = cost[1] - 1
    k = l // 2 if l % 2 == 0 else l // 2 + 1
    vis = [False] * (n + 1)

    def f(now):
        if vis[now]:
            return 0
        vis[now] = True
        c = 1
        for _, nxt in g[now]:
            c += f(nxt)

        return c

    nw = dk[1]

    cnt = []
    i = 0
    vis[1] = True
    vis[n] = True
    while i < k:
        i += 1
        nx = dk[nw]
        vis[nx] = True
        tmp = f(nw)
        vis[nx] = False
        cnt.append(tmp)
        nw = nx

    fn = 0
    q = deque([1])
    vis[1] = False

    while q:
        i = q.popleft()
        if vis[i]:
            continue

        vis[i] = True
        fn += 1
        for _, j in g[i]:
            q.appendleft(j)

    fn += sum(cnt)
    sn = n - fn

    print("Fennec" if fn > sn else "Snuke")


if __name__ == '__main__':
    main()
