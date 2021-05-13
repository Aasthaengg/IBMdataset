import collections
import sys
import numpy as np
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
MOD = 10**9+7
import itertools
import math

a = int(input())
b = int(input())
if a>b:
    print("GREATER")
elif a == b:
    print("EQUAL")
else:
    print("LESS")