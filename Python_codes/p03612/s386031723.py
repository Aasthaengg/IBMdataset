from itertools import groupby
n, *P = map(int, open(0).read().split())
c = 0
for v, g in groupby(p==i for p, i in zip(P, range(1, n+1))):
    c += v * (len(list(g))+1) // 2
print(c)