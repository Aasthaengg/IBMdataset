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
m_cnt = 0
a_cnt = 0
r_cnt = 0
c_cnt = 0
h_cnt = 0
for _ in range(n):
    s = input()
    if s[0] == 'M':
        m_cnt += 1
    elif s[0] == 'A':
        a_cnt += 1
    elif s[0] == 'R':
        r_cnt += 1
    elif s[0] == 'C':
        c_cnt += 1
    elif s[0] == 'H':
        h_cnt += 1

lst = [m_cnt, a_cnt, r_cnt, c_cnt, h_cnt]
ans = 0
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ans += lst[i] * lst[j] * lst[k]
print(ans)