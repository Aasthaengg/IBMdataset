import sys
from collections import Counter
from collections import deque
import heapq
import math
import fractions
import bisect
import itertools
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n=int(input())
p=lmp()
ans=0
for i in range(n-2):
    if sorted(list((p[i],p[i+1],p[i+2])))[1]==p[i+1]:
        ans+=1
print(ans)