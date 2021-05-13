n, k = map(int, input().split())
ab = {}
for _ in range(n):
    a, b = map(int, input().split())
    ab.setdefault(a, 0)
    ab[a] += b
keys = list(ab.keys())
keys.sort()
i = 0
for key in keys:
    i += ab[key]
    if i >= k:
        print(key)
        break