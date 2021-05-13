import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,m=mp()
a=-float("inf")
b=float("inf")
for i in range(m):
    l,r=mp()
    a=max(a,l)
    b=min(b,r)
print(max(b-a+1,0))