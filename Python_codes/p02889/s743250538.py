def warshall_floyd(n, edges):
    d = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        d[i][i] = 0
    for vf, vt, w in edges:
        d[vf][vt] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


n, m, l = map(int, input().split())
edges = []
for _ in range(m):
    a, b, w = map(int, input().split())
    if w <= l:
        edges.append((a-1, b-1, w))
        edges.append((b-1, a-1, w))
wf = warshall_floyd(n, edges)

edges.clear()
for i in range(n):
    for j in range(i + 1, n):
        if wf[i][j] <= l:
            edges.append((i, j, 1))
            edges.append((j, i, 1))
wf = warshall_floyd(n, edges)

q = int(input())
ans = [0] * q
for i in range(q):
    s, t = map(lambda x:int(x) - 1, input().split())
    ans[i] = -1 if wf[s][t] == float('inf') else wf[s][t] - 1
for x in ans:
    print(x)
