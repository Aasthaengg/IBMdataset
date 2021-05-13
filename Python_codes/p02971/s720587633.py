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
N = int(input())
A = [int(input()) for _ in range(N)]
m = max(A)
c = 0
for a in A:
    if a == m:
        c += 1
if c == 1:
    mm = 0
    for i in range(N):
        a = A[i]
        if a == m:
            continue
        mm = max(a,mm)
    for i in range(N):
        a = A[i]
        if a == m:
            print(mm)
        else:
            print(m)
else:
    for i in range(N):
        print(m)