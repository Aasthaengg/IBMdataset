import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
from itertools import accumulate
from itertools import permutations
from itertools import combinations
from collections import defaultdict
from collections import Counter
import fractions
import math
from collections import deque
from bisect import bisect_left
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
from copy import deepcopy
from decimal import Decimal
import fractions
alf = list("abcdefghijklmnopqrstuvwxyz")
ALF = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())[:-1]
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [list(input())[:-1] for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]

n,q=map(int,input().split())
s=list(input())[:-1]
lr = [list(map(int,input().split())) for _ in range(q)]
l=[0]*(n)
for i in range(1,n):
    if s[i]=='C' and s[i-1]=='A':
        l[i]=1
    else:
        l[i]=0
wa=[0]*(n)
for i in range(n):
    if i==0:
        wa[i]=0
    else:
        wa[i]=wa[i-1]+l[i]

for i in range(q):
    print(wa[lr[i][1]-1]-wa[lr[i][0]-1])
