V,M = map(int, input().split())
abc = [list(map(int, input().split())) for i in range(M)]
G = [list() for i in range(V)]
for a,b,c in abc:
    G[b-1].append((a-1,-c))
INF = 10**18
dist = [INF] * V
dist[V-1] = 0
update = 1
for _ in range(V):
    update = 0
    for v, e in enumerate(G):
        for t, cost in e:
            if dist[v] != INF and dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                update = 1
    if not update:
        break
else:
    print('inf')
    exit()
print(-dist[0])