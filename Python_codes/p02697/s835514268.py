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

n,m = LI()
if n % 2:
    for i in range(m):
        print(i+1, n-i-1)
else:
    flag = False
    for i in range(m):
        if not flag and (n-i-1) - (i+1) <= n // 2:
            flag = True
        if flag:
            print(i+1, n-i-2)
        else:
            print(i+1, n-i-1)



