import sys
import math,bisect
sys.setrecursionlimit(10 ** 5)
from collections import defaultdict
from itertools import groupby,accumulate
from heapq import heapify,heappop,heappush
from collections import deque,Counter,OrderedDict
def I(): return int(sys.stdin.readline())
def neo(): return map(int, sys.stdin.readline().split())
def Neo(): return list(map(int, sys.stdin.readline().split()))
n = I()
A,B = [],[]
for i in range(n):
    a,b = neo()
    A += [a+b]
    B += [a-b]
A.sort()
B.sort()
Ans = max(A[-1]-A[0],B[-1]-B[0])
print(Ans)
