def bellman_ford(a, v, e):
    inf = pow(2, 61) - 1
    dist = [inf] * v
    dist[a] = 0
    for i in range(2 * v):
        f = 0
        for s, t, d in E:
            if not dist[s] == inf and dist[t] > dist[s] + d:
                dist[t] = dist[s] + d
                f = 1
        if not f:
            x0 = dist[-1]
            break
        elif f and i == v - 1:
            x0 = dist[-1]
    if x0 == dist[-1]:
        return -dist[-1]
    else:
        return "inf"

n, m = map(int, input().split())
E = []
for _ in range(m):
    a, b, c = map(int, input().split())
    E.append([a - 1, b - 1, -c])
ans = bellman_ford(0, n, m)
print(ans)