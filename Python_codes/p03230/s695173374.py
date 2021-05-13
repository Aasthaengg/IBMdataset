#!/usr/bin/env python3
#Tenka1 Programmer Beginner Contest D

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

n = I()
lst = [3]
tmp = 3
if n == 1:
    print('Yes')
    print(2)
    print(1,1)
    print(1,1)
    quit()
for _ in range(500):
    x = lst[-1] + tmp
    lst.append(x)
    tmp += 1
if n not in lst:
    print('No')
else:
    print('Yes')
    x = lst.index(n) + 3
    print(x)
    lst = [[] for _ in range(x-1)]
    tmp = 0
    cnt = 0
    for i in range(1,n+1):
        lst[tmp].append(i)
        if cnt == tmp:
            tmp += 1
            cnt = 0
            continue
        cnt += 1
    ans = [[] for _ in range(x)]
    tmp = 0
    for i in range(x-1):
        for j in range(tmp):
            ans[i].append(lst[tmp][j])
        for j in range(tmp,x-1):
            ans[i].append(lst[j][tmp])
        tmp += 1
    for i in range(x-1):
        ans[-1].append(lst[i][-1])
    for i in range(x):
        print(x-1,*ans[i])
