import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
MOD = 10**9+7
import itertools
import math

a,b,c,k = map(int,input().split())
if k%2 == 0:
    print(a-b)
elif k%2 == 1:
    print(b-a)
elif abs(a-b)>10**18:
    print("Unfair")