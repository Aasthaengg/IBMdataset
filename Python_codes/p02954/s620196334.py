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

S=input()
L=[0]*len(S)
S=S+"X"
r=0
l=0
i=0
ind=0
c=True
for s in S:
    if c:
        if s=="R":
            r+=1
        else:
            ind=i
            c=False
            l+=1
    else:
        if s=="L":
            l+=1
        else:
            L[ind]+=r//2
            L[ind-1]+=r-r//2
            L[ind]+=l-l//2
            L[ind-1]+=l//2
            c=True
            r,l=1,0
    i+=1
print(*L)