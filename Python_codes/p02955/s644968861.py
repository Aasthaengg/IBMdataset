#!/usr/bin/env python3
#ABC136 E

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

n,k = map(int,input().split())
a = list(map(int,input().split()))
s = sum(a)
lst = []
for i in range(1,int(math.sqrt(s))+1):
    if s % i == 0:
        if i != s//i:
            lst.append(i)
            lst.append(s//i)
        else:
            lst.append(i)
lst.sort()
for i in lst[::-1]:
    x = [[j%i,-j%i] for j in a]
    x.sort()
    b = [j for j,k in x]
    c = [k for j,k in x]
    #+1をするリスト
    b = list(accumulate(b))
    #-1をするリスト
    c = list(accumulate(c))
    for j in range(n-1):
        if b[j] == c[-1]-c[j]:
            ans = b[j]
            break
    if ans <= k:
        print(i)
        break
