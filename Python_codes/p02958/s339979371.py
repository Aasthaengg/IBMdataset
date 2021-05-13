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
a=sorted(p)
c=0
for i in range(n):
    if p[i]!=a[i]:
        c+=1
if c==2 or c==0:
    print("YES")
else:
    print("NO")