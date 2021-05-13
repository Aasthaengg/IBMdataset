from bisect import bisect_right
n, m = map(int, input().split())
py = [tuple(map(int, input().split())) for _ in range(m)]
d = dict()
for p, y in py:
    if p not in d.keys():
        d[p] = [y]
    else:
        d[p].append(y)

for v in d.values():
    v.sort()

for p, y in py:
    print(str(p).zfill(6) + str(bisect_right(d[p], y)).zfill(6))
