import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
MOD = 10**9+7

a,b,c = map(int,input().split())
s = set([a,b,c])
print(len(s))