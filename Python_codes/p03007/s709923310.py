#!/usr/bin/env python3
#diverta2019_2 C

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

n = int(input())
a = list(map(int,input().split()))
a.sort()
ma = a[-1]
mi = a[0]
log = []
for i in a[1:-1]:
    if i >= 0:
        log.append([mi,i])
        mi -= i
    else:
        log.append([ma,i])
        ma -= i
log.append([ma,mi])
print(ma-mi)
for i in range(n-1):
    x,y = log[i]
    print(x,y)
