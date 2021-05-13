#!/usr/bin/env python3
#CODEFESTIVAL2016 qualC C

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

n = I()
t = LI()
a = LI()
x = [0]*n
y = [0]*n
if a[0] != t[-1]:
    print(0)
    quit()
for i in range(1,n):
    if t[i] > t[i-1]:
        x[i] = 1
for i in range(1,n)[::-1]:
    if a[i] < a[i-1]:
        y[i-1] = 1
ans = 1
for i in range(1,n-1):
    if x[i] == 1 and y[i] == 1:
        if t[i] != a[i]:
            print(0)
            quit()
    elif x[i] == 1:
        if a[i] < t[i]:
            print(0)
            quit()
    elif y[i] == 1:
        if a[i] > t[i]:
            print(0)
            quit()
    else:
        ans *= min(t[i],a[i])
        ans %= mod
print(ans)
