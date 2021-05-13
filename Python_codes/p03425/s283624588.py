import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n = ri()
c = collections.Counter([rr()[0] for _ in range(n)])
d = [v for k, v in c.items() if k in 'MARCH']
ans = 0
if len(d) >= 3:
    for lis in itertools.combinations(d, 3):
        a, b, c = lis
        ans += a*b*c
    print(ans)
else:
    print(0)
