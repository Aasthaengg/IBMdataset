def Bellman_Ford(G, start, goal):
    V = len(G)
    INF = float('inf')
    negative = [False] * V
    dist = [INF] * V
    dist[start] = 0
    for i in range(V-1):
        UnUpdate = True
        for v, e in enumerate(G):
            for t, cost in e:
                if dist[v] != INF and dist[v] + cost < dist[t]:
                    dist[t] = dist[v] + cost
                    UnUpdate = False
        if UnUpdate:
            break

    if not UnUpdate:
        for i in range(V):
            UnUpdate = True
            for v, e in enumerate(G):
                for t, cost in e:
                    if dist[v] != INF and dist[v] + cost < dist[t]:
                        dist[t] = dist[v] + cost
                        negative[t] = True
                        for tt, cct in G[t]:
                            negative[tt] = True
                        UnUpdate = False

            if UnUpdate or negative[goal]:
                break
    if negative[goal]:
        return "inf"
    else:
        return 0-dist[goal]


V, E = map(int, input().split())
G = [[] for i in range(V)]
for i in range(E):
    a, b, c = map(int, input().split())
    G[a-1].append((b-1, 0-c))
ans = Bellman_Ford(G,0,V-1)
print(ans)