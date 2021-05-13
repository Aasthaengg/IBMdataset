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

n=int(input())
l=list(Counter(lmp()).items())
ans=0
for q in l:
    if q[0]>q[1]:
        ans+=q[1]
    elif q[0]<q[1]:
        ans+=q[1]-q[0]
print(ans)