n, m = map(int, input().split())
par = list(range(n))


def find(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x


def union(x, y):
    x1 = find(x)
    y1 = find(y)
    if x1 != y1:
        par[x1] = y1


for j in range(m):
    a, b = map(int, input().split())
    union(a - 1, b - 1)

s = [0 for i in range(n + 1)]

for k in range(n):
    s[find(k)] += 1


print(max(s))
