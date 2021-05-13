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

t1,t2 = LI()
a1,a2 = LI()
b1,b2 = LI()

x,y = a1*t1,b1*t1
z,w = a1*t1 + a2*t2, b1*t1 + b2*t2
if (x > y and z > w) or (y > x and w > z):
    print(0)
    quit()
if (z == w) :
    print('infinity')
    quit()
if x < y:
    x,y = y,x
if z < w:
    z,w = w,z
s1 = x - y
s2 = z - w
p = math.ceil(s1/s2)
q = s1 % s2
ans = 2*p - (q != 0)
print(ans)
