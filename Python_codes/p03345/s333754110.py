#!/usr/bin/env python3
#AGC24 A

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
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

a,b,c,k = LI()
s,t,u = b+c,a+c,a+b
x,y,z = t+u,s+u,s+t
if k % 2:
    print(s-t)
else:
    print(x-y)
