n, k = map(int, input().split())
A = tuple(map(int, input().split()))
d = dict()
for a in A:
    d.setdefault(a, 0)
    d[a] += 1

cs = sorted(list(d.values()))

if len(cs) <= k:
    print(0)
else:
    c = 0
    print(sum(cs[:-k]))
