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
for i in range(10**7):
    if i*(i+1)>=2*n:
        m=i
        c=i*(i+1)//2-n
        break
for i in range(1,m+1):
    if i!=c:
        print(i)