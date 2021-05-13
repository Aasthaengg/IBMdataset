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
p.append(n+1)
ans=0
for i in range(n):
    if p[i]==i+1:
        p[i],p[i+1]=p[i+1],p[i]
        ans+=1
print(ans)