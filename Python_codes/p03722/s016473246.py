n, m = map(int, input().split())
edges = [None] * m

for i in range(m):
    a, b, c = map(int, input().split())
    edges[i] = (a-1, b-1, -c)

INF = float("inf")
d = [INF] * n
d[0] = 0

for i in range(n-1):
    for f, t, c in edges:
        if d[f] == INF: continue
        d[t] = min(d[t], d[f] + c)

inf_flag = [False] * n

for i in range(n):
    for f, t, c in edges:
        if d[f] == INF: continue
        if inf_flag[f] == True:
            inf_flag[t] = True
        if d[t] > d[f] + c:
            d[t] = d[f] + c
            inf_flag[t] = True

print("inf" if inf_flag[n-1] else -d[n-1])
