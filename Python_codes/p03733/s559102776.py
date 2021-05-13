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

n,T=mp()
t=lmp()
ans=0
for i in range(1,n):
    if T<t[i]-t[i-1]:
        ans+=T
    else:
        ans+=t[i]-t[i-1]
print(ans+T)