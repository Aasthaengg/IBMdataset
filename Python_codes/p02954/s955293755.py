from itertools import groupby
from math import ceil

s = input()

res = []
a = [sum(1 for _ in it) for k, it in groupby(s)]
it = iter(a)
for r, l in zip(it, it):
    res.extend([0]*r)
    res[-1] += ceil(r/2) + l//2

    res.extend([0]*l)
    res[-l] += r//2 + ceil(l/2)

print(' '.join(map(str, res)))
