#!/usr/bin/env python3
#ABC82 D

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

s = input()
n = len(s)
x,y = LI()
lst = []
tmp = 0
for i in range(n):
    if s[i] == 'T':
        lst.append(tmp)
        tmp = 0
    else:
        tmp += 1
if s[-1] != 'T':
    lst.append(tmp)
m = len(lst)
dpx = defaultdict(int)
dpy = defaultdict(int)
dpx[0] = True
dpy[0] = True
for i in range(m):
    if i % 2:
        tmp = defaultdict(int)
        for k in dpy.keys():
            tmp[k + lst[i]] = True
            tmp[k - lst[i]] = True
        dpy = tmp
    else:
        tmp = defaultdict(int)
        if i == 0:
            for k in dpx.keys():
                tmp[k + lst[i]] = True
        else:
            for k in dpx.keys():
                tmp[k + lst[i]] = True
                tmp[k - lst[i]] = True
        dpx = tmp
if dpx[x] and dpy[y]:
    print('Yes')
else:
    print('No')