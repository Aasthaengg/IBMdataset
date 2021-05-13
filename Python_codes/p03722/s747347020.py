INF = float("inf")

def bellman_ford(edges, n, s):
    d = [0] + [INF] * (n-1)
    for i in range(n):
        for f, t, c in edges:
            if d[f] == INF: continue
            if d[t] > d[f] + c:
                if i == n-1: d[t] = -INF
                else: d[t] = d[f] + c
    for i in range(n):
        for f, t, c in edges:
            if d[f] == INF: continue
            d[t] = min(d[t], d[f] + c)
    return d

n, m = map(int, input().split())
es = [None] * m
for i in range(m):
    f, t, c = map(int, input().split())
    es[i] = (f-1, t-1, -c)

d = bellman_ford(es, n, 0)
print(-d[n-1])
