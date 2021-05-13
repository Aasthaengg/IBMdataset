import bisect

a, b, q = list(map(int, input().split(' ')))
inf = float('inf')

sa = [None] * a
for i in range(a):
    sa[i] = (int(input()))

tb = [None] * b
for i in range(b):
    tb[i] = (int(input()))

xq = [None] * q
for i in range(q):
    xq[i] = (int(input()))

sa = [-inf] + sa + [inf]
tb = [-inf] + tb + [inf]

for x in xq:
    result = float('inf')

    l = bisect.bisect_left(sa, x)
    m = bisect.bisect_left(tb, x)

    for v in [sa[l - 1], sa[l]]:
        for w in [tb[m - 1], tb[m]]:
            o = abs(x - v) + abs(v - w)
            p = abs(x - w) + abs(w - v)
            result = min(result, o, p)

    print(result)

