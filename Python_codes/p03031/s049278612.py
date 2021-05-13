import numpy as np
import itertools
n,m = map(int, input().split())
sw = [[int(i) - 1 for i in input().split()] for _ in range(m)]
p = np.array([int(i) for i in input().split()])
x = np.full_like(p, -1)

s_l = itertools.product(np.array([True,False]), repeat = n)
ans = 0
for si in s_l:
    si = np.array(si)
    for mi in range(m):
        x[mi] = si[sw[mi][1:]].sum() % 2
    if np.all(p == x):
        ans += 1
print(ans)