#!/usr/bin/env python3
#CADDi D

import sys
import math
import bisect
sys.setrecursionlimit(1000000000)
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n = I()
a = [I() for _ in range(n)]
flg = 0
for i in a:
    if i % 2:
        flg = 1
if flg == 0:
    print('second')
else:
    print('first')
