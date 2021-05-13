n, m = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)
for i in range(1, n - 1):
    ma = 0
    mi = n
    for node in g[i]:
        ma = max(ma, node)
        mi = min(mi, node)
    if ma == n - 1 and mi == 0:
        print('POSSIBLE')
        break
else:
    print('IMPOSSIBLE')
