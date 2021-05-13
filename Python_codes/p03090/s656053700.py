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
a = [i+1 for i in range(N)]
li = list(itertools.combinations(a,2))
n = len(li)
if N % 2 == 1:
    print(N*(N-1)//2-N//2)
else:
    print(N*(N-1)//2-N//2)
for i in range(n):
    a,b = li[i]
    if N % 2 == 1:
        if a+b != N:
            print(a,b)
    else:
        if a+b != N+1:
            print(a,b)
