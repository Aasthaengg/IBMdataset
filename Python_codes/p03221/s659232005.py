import bisect

n, m = map(int, input().split())
li = []
d = {}
for _ in range(m):
    p, y = map(int, input().split())
    li.append([p, y])
    if p not in d:     
        d[p] = [y]
    else:
        d[p].append(y)
for k, v in d.items():
    v.sort()
for p, y in li:
    r = bisect.bisect_right(d[p], y)
    print(str(p).zfill(6) + str(r).zfill(6))
