n,m = map(int,input().split( ))

E = [[] for _ in range(n+1)]
for i in range(m):
    ai,bi,ci = map(int, input().split( ))
    ai-=1;bi-=1
    E[ai].append((bi,-ci))
#「nまでの経路で」負閉路が要る
#https://tjkendev.github.io/procon-library/python/graph/bellman-ford.html
# V: グラフの頂点数
# r: 始点
# G[v] = [(w, cost), ...]: 頂点vからコストcostで到達できる頂点w
INF = 10**18
dist = [INF] * n
dist[0] = 0
update = 1
for _ in range(n):
    update = 0
    for v, e in enumerate(E):
        for t, cost in e:
            if dist[v] != INF and dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                update = 1
    if not update:
        break

ans = dist[n-1]


for _ in range(n):
    update = 0
    for v, e in enumerate(E):
        for t, cost in e:
            if dist[v] != INF and dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                update = 1
if ans > dist[n-1]:
    print("inf")
else:
    print(-ans)###-

