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
l=[]
for i in range(n):
    l.append(lmp())
l=sorted(l,key=lambda x:x[1])
t=0
for i in range(n):
    t+=l[i][0]
    if t>l[i][1]:
        print("No")
        exit()
print("Yes")