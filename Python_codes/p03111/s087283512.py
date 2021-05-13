from collections import defaultdict
from itertools import combinations, permutations
from operator import itemgetter
n, a, b, c, *L = map(int, open(0).read().split())
L.sort()
A = [a, b, c]
dicts = [defaultdict(lambda: 10**5) for _ in range(3)]
for i in range(n-2):
    for x in combinations(enumerate(L), i+1):
        k = tuple(i for i, l in x)
        v = sum(l for i, l in x)
        for d, x in zip(dicts, A):
            d[k] = min(d[k], abs(x-v) + 10*i)
scores = [sorted(d.items(), key=itemgetter(1)) for d in dicts]

ans = 10**5
for p1, p2, p3 in permutations(range(3)):
    k1, v1 = scores[p1][0]
    k1 = set(k1)
    for k2, v2 in scores[p2]:
        k2 = set(k2)
        if len(k1 & k2) == 0:
            break
    for k3, v3 in scores[p3]:
        k3 = set(k3)
        if len(k1 & k3) + len(k2 & k3) == 0:
            break
    ans = min(ans, sum([v1, v2, v3]))
print(ans)