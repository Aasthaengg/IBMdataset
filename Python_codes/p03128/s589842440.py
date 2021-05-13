#!/usr/bin/env python3
#ABC118 D

import sys
import math
import bisect
from heapq import heappush, heappop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
mod = 10**9 + 7

M = [0,2,5,5,4,5,6,3,7,6]
n,m = map(int,input().split())
a = list(map(int,input().split()))
A = [[i,M[i]] for i in a]
A.sort(key = itemgetter(1))

#dp[i] := ちょうどマッチi本を使ってできる最大桁数
dp = [-float('inf')]*(n+1)
dp[0] = 0
for i in range(n):
    for j,k in A:
        if i + k < n+1:
            if dp[i] < 0:
                continue
            dp[i+k] = dp[i] + 1
A.sort(key = itemgetter(0),reverse = True)
ans = ''
k = n
while 1:
    for i,j in A:
        if k - j < 0:
            continue
        if dp[k-j] == dp[k]-1:
            ans += str(i)
            k -= j
            break
    else:
        break
print(ans)
