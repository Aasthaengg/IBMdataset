import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

a,b = map(int,input().split())
if a+b>=10:
    print("error")
else:
    print(a+b)