n, m = map(int, input().split())
cs = [[float('inf')] * n for _ in range(n)]
ns = [[0] * n for _ in range(n)]
for i in range(n):
    cs[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    cs[a][b] = cs[b][a] = c
    ns[a][b] = b
    ns[b][a] = a
for k in range(n):
    for i in range(n):
        for j in range(n):
            s = cs[i][k] + cs[k][j]
            if s < cs[i][j]:
                cs[i][j] = s
                ns[i][j] = ns[i][k]
used = set()
for i in range(n):
    for j in range(i + 1, n):
        path = [i]
        while path[-1] != j:
            s = path[-1]
            t = ns[s][j]
            path.append(t)
            used.add(tuple(sorted([s, t])))
print(m - len(used))