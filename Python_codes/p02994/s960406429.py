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

n,l=mp()
x=0
if l>0:
    x=l
elif l+n-1<0:
    x=l+n-1
print((l-1)*n+n*(n+1)//2-x)