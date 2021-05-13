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

a=int(input())
b=int(input())
c=int(input())
x=int(input())
ans=0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500*i+100*j+50*k==x:
                ans+=1
print(ans)