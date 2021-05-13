from heapq import heappush, heappop

INF = 10**15

def dijkstra(s, edges):
    n = len(edges)
    que = []
    d = [INF] * n
    prev = [-1] * n
    d[s] = 0
    heappush(que, (0, s))

    while len(que) > 0:
        (c, v) = heappop(que)
        if d[v] < c:
            continue
        for (cc, w) in edges[v]:
            if d[w] > d[v] + cc:
                d[w] = d[v] + cc
                prev[w] = v
                heappush(que, (d[w], w))

    return d, prev

n = int(input())
edge = [[] for i in range(n)]
for i in range(n-1):
    ai, bi, ci = map(int, input().split())
    ai, bi = ai-1, bi-1
    edge[ai].append((ci, bi))
    edge[bi].append((ci, ai))

q, k = map(int, input().split())
x, y = [], []
for i in range(q):
    xi, yi = map(int, input().split())
    xi, yi = xi-1, yi-1
    x.append(xi)
    y.append(yi)

dist, prev = dijkstra(k-1, edge)

for i in range(q):
    print(dist[x[i]]+dist[y[i]])