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
p=lmp()
ans=0
m=2*n
for i in range(n):
    if p[i]<=m:
        ans+=1
        m=p[i]
print(ans)