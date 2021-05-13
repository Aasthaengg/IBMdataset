N, M = map(int, input().split())
F = [list(map(int, input().split())) for i in range(M)]

d = [-1]*N


def find(x):
    if d[x] < 0:
        return x
    d[x] = find(d[x])
    return d[x]


def union(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if (d[x] > d[y]):
        x, y = y, x
    d[x] += d[y]
    d[y] = x


for f in F:
    union(f[0]-1, f[1]-1)
print(-min(d))
