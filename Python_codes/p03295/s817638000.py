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
ab=sorted([lmp() for i in range(m)],key=itemgetter(1))
removed=-1
ans=0
for a,b in ab:
    if a>removed:
        removed=b-1
        ans+=1
print(ans) 