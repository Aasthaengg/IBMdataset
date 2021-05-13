N, K = map(int, input().split())
d = dict()
for _ in range(N):
    a, b = map(int, input().split())
    d[a] = d.get(a, 0) + b
for key in sorted(d.keys()):
    c = d[key]
    if K <= c:
        break
    K -= c
print(key)