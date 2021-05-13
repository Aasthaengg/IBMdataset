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

N=int(input())
for h in range(1,3501):
    for n in range(h,3501):
        if (4*h*n-N*n-N*h)!=0:
            if (N*h*n)%(4*h*n-N*n-N*h)==0 and (N*h*n)//(4*h*n-N*n-N*h)>0:
                print(h,n,(N*h*n)//(4*h*n-N*n-N*h))
                exit()