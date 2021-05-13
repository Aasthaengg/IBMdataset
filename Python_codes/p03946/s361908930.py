n, t = map(int, input().split())
A = list(map(int, input().split()))
d = {}
min_ = 10**18
for a in A:
    p = a-min_
    if p not in d:
        d[p] = 1
    else:
        d[p] += 1
    if a <= min_:
        min_ = a
M = max(d.keys())
print(d[M])
