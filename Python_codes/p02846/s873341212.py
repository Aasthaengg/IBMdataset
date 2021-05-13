#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
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

t1, t2 = LI()
a1, a2 = LI()
b1, b2 = LI()

a = a1 * t1 + a2 * t2
b = b1 * t1 + b2 * t2

if a == b:
    print('infinity')
else:
    if b > a:
        if a1 * t1 < b1 * t1:
            print(0)
        elif a1 * t1 == b1 * t1:
            print(1)
        elif a1 * t1 > b1 * t1:
            c = b - a
            d = a1 * t1 - b1 * t1
            e = d % c != 0
            print(2 * (d // c) + e)
    else:
        if b1 * t1 < a1 * t1:
            print(0)
        elif b1 * t1 == a1 * t1:
            print(1)
        elif b1 * t1 > a1 * t1:
            c = a - b
            d = b1 * t1 - a1 * t1
            e = d % c != 0
            print(2 * (d // c) + e)
