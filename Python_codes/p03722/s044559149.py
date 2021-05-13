import sys
n, m = [int(i) for i in sys.stdin.readline().split()]
graph = {i : [] for i in range(n)}
edge_ls = []
for i in range(m):
    a, b, c = [int(i) for i in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    graph[a].append((b, c))
    edge_ls.append((a, b, c))

INF = float("inf")
d = [-INF for i in range(n)]
d[0] = 0
res = True
before_ls = [i for i in range(n)]
for i in range(n):
    flg = False
    for _from, _to, cost in edge_ls:
        if d[_to] < d[_from] + cost and d[_from] != -INF:
            d[_to] = d[_from] + cost
            before_ls[_to] = _from
            if i == n - 1 and _to == n-1:
                flg = True
if flg:
    print("inf")
else:
    print(d[-1])