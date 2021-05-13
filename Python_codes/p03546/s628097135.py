import heapq
INF = 10**10


def dijkstra(s, G):
    d = [INF] * len(G)
    d[s] = 0
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, s))
    while len(q) > 0:
        shortest, v = heapq.heappop(q)
        if d[v] < shortest:
            continue
        for e in G[v]:
            to, cost = e
            if d[to] > d[v] + cost:
                d[to] = d[v] + cost
                heapq.heappush(q, (d[to], to))
    return d


H, W = map(int, input().split())
G = [[] for _ in range(10)]
for i in range(10):
    adj = list(map(int, input().split()))
    for j, cost in enumerate(adj):
        # 1からの距離を計算したいから逆向きのグラフを考える
        G[j].append((i, cost))
shortest_d = dijkstra(1, G)
ans = 0
for _ in range(H):
    for x in list(map(int, input().split())):
        if x == -1:
            continue
        ans += shortest_d[x]
print(ans)
