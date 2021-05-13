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
S = list(input())[:-1]
table = [0]*(N+5)
table[1] = 1
for i in range(2,N+3):
    num = i
    cnt = 0
    while num != 0:
        a = num % 2
        num = num // 2
        cnt += a
    p = i % cnt
    table[i] = table[p]+1
c = 0
for s in S:
    if s == "1":
        c += 1
p = 0
q = 0

for i in range(N):
    ss = S[N-1-i]
    p += int(ss)*pow(2,i,c+1)
    if c != 1:
        q += int(ss)*pow(2,i,c-1)
    p %= (c+1)
    if c != 1:
        q %= (c-1)
for i in range(N):
    ss = S[i]
    if ss == "0":
        ans = (p+pow(2,N-1-i,c+1))%(c+1)
        print(table[ans]+1)
    else:
        if c == 1:
            print(0)
        else:
            if c != 1:
                ans = (q-pow(2,N-1-i,c-1))%(c-1)
                print(table[ans]+1)
            else:
                print(0)
        
