import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections

a,op,b = input().split()
a = int(a)
b = int(b)
if op == "+":
    print(a+b)
else:
    print(a-b)