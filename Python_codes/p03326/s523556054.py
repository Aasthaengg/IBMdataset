(n,m),*xyzs = [list(map(int, s.split())) for s in open(0)]

from operator import mul
from itertools import product, starmap
ans = -float('inf')
for ptrns in product([-1, 1], repeat=3):
    tmp = [sum(starmap(mul, zip(xyz, ptrns))) for xyz in xyzs]
    tmp.sort(reverse=True)
    ans = max(ans, sum(tmp[:m]))

print(ans)