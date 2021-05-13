#!/usr/bin/env python3
#ABC140 E
#類題 AGC5 B

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

lst = LI()
if lst.count(1) == 1:
    if lst.count(7) == 1:
        if lst.count(9) == 1:
            if lst.count(4) == 1:
                print('YES')
                quit()
print('NO')

