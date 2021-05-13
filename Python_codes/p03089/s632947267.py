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
b = LI()
flag = [True] * n
ans = []
for i in range(n):
    cnt = 0
    idx = -1
    for j in range(n):
        if flag[j]:
            cnt += 1
            if b[j] == cnt:
                idx = j
    if idx == -1:
        print(-1)
        quit() 
    flag[idx] = False
    ans.append(b[idx])
for i in ans[::-1]:
    print(i)