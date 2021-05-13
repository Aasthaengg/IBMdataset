#!/usr/bin/env python3
#ABC90 D

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


n,k = map(int,input().split())

ans = 0
for i in range(1,n+1):
    p = n//i
    r = n%i
    ans += p*max(0,i-k) + max(0,r-k+1)
if k == 0:
    ans = n**2
print(ans)
