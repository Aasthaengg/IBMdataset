n, m = map(int, input().split())
d = [[] for _ in range(n)]
for i in range(m):
    p, y = map(int, input().split())
    d[p-1].append((y, i))
d = list(map(sorted, d))
ans = [0] * m
for p in range(n):
    for x, (y, i) in enumerate(d[p], 1):
        ans[i] = (p + 1) * 10 ** 6 + x
for a in ans:
    print(str(a + 10 ** 12)[1:])
