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

n = I()
s = input()
ans = 0
for i in range(1000):
    t1, t2, t3 = list("00" + str(i))[-3:]
    f1, f2, f3 = False, False, False
    for j in range(n):
        if not f1 and s[j] == t1:
            f1 = True
        elif f1 and not f2 and s[j] == t2:
            f2 = True
        elif f2 and not f3 and s[j] == t3:
            f3 = True

    if f3:
        ans += 1
print(ans)