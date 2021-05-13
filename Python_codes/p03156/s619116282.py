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
a,b=mp()
p=lmp()
ans=[0,0,0]
for i in p:
    if i<=a:
        ans[0]+=1
    elif i<=b:
        ans[1]+=1
    else:
        ans[2]+=1
print(min(ans))