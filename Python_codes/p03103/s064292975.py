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
N,M = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
ans = 0
index = 0
C = sorted(AB,key = lambda x:x[0])
while M > 0:
    if C[index][1] < M:
        ans += C[index][1]*C[index][0]
        M -= C[index][1]
        index += 1
    else:
        ans += M*C[index][0]
        M = 0
print(ans)