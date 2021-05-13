import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9 + 7

a,b,c = map(int,input().split())
if a <= c and c <= b:
    print("Yes")
else:
    print("No")