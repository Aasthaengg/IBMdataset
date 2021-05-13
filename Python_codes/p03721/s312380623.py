n, k = map(int, input().split())
d = {}
for _ in range(n):
    a, b = map(int, input().split())
    if a in d:
        d[a] += b
    else:
        d[a] = b
d = dict(sorted(d.items()))
cnt = 0
for key, v in d.items():
    cnt += v
    if cnt >= k:
        print(key)
        break