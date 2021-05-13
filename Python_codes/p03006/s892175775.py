import itertools
from collections import Counter
n = int(input())
xy = [[int(x) for x in input().split()] for _ in range(n)]
vectors = []
for xy1, xy2 in itertools.combinations(xy,2):
    p = xy2[0] - xy1[0]
    q = xy2[1] - xy1[1]
    vectors.append((p, q))
    vectors.append((-p, -q))
c = Counter(vectors)
if n>=2:
    x = max(c.values())
    res = n - x
else:
    res = 1
print(res)