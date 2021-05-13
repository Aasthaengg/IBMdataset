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

"""
累積和をとる⇒各要素をmで割った余りを出す
同じ余りの場合、その間はkの倍数になっている
同じ余りのものを2つ選ぶ総数
"""
n,m = LI()
a = LI()
a = list(accumulate(a))
lst = [0] + [i % m for i in a]
lst = list(Counter(lst).items())
ans = 0
for i,j in lst:
    if j >= 2:
        ans += j*(j-1)//2
print(ans)