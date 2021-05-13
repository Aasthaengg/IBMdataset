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
alf = list("abcdefghijklmnopqrstuvwxyz")
ALF = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = 0
for i in range(N):
    if V[i]-C[i]>0:
        ans += V[i]-C[i]
print(ans)
