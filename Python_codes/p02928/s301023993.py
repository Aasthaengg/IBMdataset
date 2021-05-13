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
from bisect import bisect_right
from bisect import insort_left
import itertools
from heapq import heapify
from heapq import heappop
from heapq import heappush
import heapq
from copy import deepcopy
from decimal import Decimal
alf = list("abcdefghijklmnopqrstuvwxyz")
ALF = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
MOD = 10**9+7
N,K = map(int,input().split())
A = list(map(int,input().split()))
d = defaultdict(int)
for a in A:
    d[a] += 1
ans = 0
for i in range(1,2001):
    c = 0
    for j in range(0,i):
        c += d[j]
    ans += c*d[i]*((K-1)*K)//2
    ans %= MOD
for i in range(len(A)):
    a = A[i]
    for j in range(i+1,len(A)):
        if a > A[j]:
            ans += K
ans %= MOD
print(ans)
