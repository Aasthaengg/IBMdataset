from collections import defaultdict, deque
import sys, heapq, bisect, math, itertools, string, queue, copy, time
from fractions import gcd
import numpy as np
sys.setrecursionlimit(10**8)
INF = float('inf')
MOD = 10**9+7
EPS = 10**-7

a, b = map(int, input().split())

big = 100000
ans = big + 1
for i in range(big, 0, -1):
    if int(i*0.08) == a and int(i*0.1) == b:
        ans = i
    
if ans <= big:
    print(ans) 
else:
    print(-1)