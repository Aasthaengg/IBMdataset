n, m = map(int, input().split())
g = [[] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)

for path in g:
    print(len(path))
