import sys
import numpy as np
import math
import collections
import copy
from collections import deque 
from functools import reduce
from itertools import product

# input = sys.stdin.readline

D, G = map(int, input().split())
pc = [list(map(int, input().split())) for _ in range(D)]
ans = 10**8
for p in product((0, 1), repeat=D):
    nmax = -1
    num = 0
    total = 0
    need = 0
    for i, pi in enumerate(p):
        if pi == 1:
            num += pc[i][0]
            total += pc[i][0]*(i+1)*100 + pc[i][1]
        else:
            nmax = i
#     print(p)
#     print(nmax, num, total)
    if total < G:
        if nmax < 0:
            continue
        if total + nmax * 100 * pc[nmax][0] + pc[nmax][1] < G:
            continue
        need = math.ceil((G-total) / ((nmax+1)*100))
    ans = min(ans, num+need)
#     print(nmax, num, total, need, ans)

print(ans)



