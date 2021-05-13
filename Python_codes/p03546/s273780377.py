def warshall_floyd(d):
    # d[i][j]: The shortest distance from i to j
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


h, w = map(int, input().split())

c = [[] for _ in range(10)]
a = [[] for _ in range(h)]

for i in range(10):
    c[i] = list(map(int, input().split()))

for i in range(h):
    a[i] = list(map(int, input().split()))

warshall_floyd(c)

ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] != -1 and a[i][j] != 1:
            ans += c[a[i][j]][1]

print(ans)

