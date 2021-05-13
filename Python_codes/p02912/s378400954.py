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
a=lmp()
l=[]
heapq.heapify(l)
for i in a:
    heapq.heappush(l,(-1)*i)
for i in range(m):
    j=heapq.heappop(l)
    heapq.heappush(l,-(-j//2))
print(-sum(l))