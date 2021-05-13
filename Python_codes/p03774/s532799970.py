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
rf = lambda: map(float, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n, m = rm()
stu = [rl() for _ in range(n)]
poi = [rl() for _ in range(m)]
for lis in stu:
    x, y = lis
    min_ = inf
    ans = ''
    for idx, li in enumerate(poi, 1):
        x1, y1 = li
        t = abs(x1-x)+abs(y1-y)
        if min_ > t:
            min_ = t
            ans = idx
    print(ans)







