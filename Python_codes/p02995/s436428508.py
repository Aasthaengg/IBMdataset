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

a, b, c, d = LI()
ans = b - a + 1
lcm = c * d // math.gcd(c, d)
ans -= b // c - ((a-1) // c + 1) + 1
ans -= b // d - ((a-1) // d + 1) + 1
ans += b // lcm - ((a-1) // lcm + 1) + 1
print(ans)