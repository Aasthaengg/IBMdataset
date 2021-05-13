dd = {}
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    dd[a] = dd.get(a,0) + 1
    dd[b] = dd.get(b,0) + 1
for i in range(1, n+1):
    print(dd.get(i, 0))