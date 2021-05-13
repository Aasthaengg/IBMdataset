import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
MOD = 10**9+7
import itertools
import math

n,a,b = map(int,input().split())

if a%2 == b%2:
    print((b-a)//2)
    sys.exit()
else:
    c = min(a-1,n-b) + 1
    ans = c + (b-a-1)//2
    print(ans)
    sys.exit()