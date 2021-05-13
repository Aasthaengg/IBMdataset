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
fr = [[] for _ in range(N)]

AB = [list(map(int,input().split())) for _ in range(M)]
for i in range(M):
    a,b = AB[i]
    a,b = a-1,b-1
    fr[a].append(b)
    fr[b].append(a)
def dfs(fr,cur,parent,index,li):
    children = fr[cur]
    for chi in children:
        if chi == parent or used[chi] != -1:
            continue
        used[chi] = index
        li.append(chi)
        dfs(fr,chi,cur,index,li)
cnt = 0
for i in range(M):
    a,b = AB[i]
    a,b = a-1,b-1
    used = [-1]*N #-1なら未探索。数字はrenketuのindex
    renketu = []
    index = 0
    fr[a].remove(b)
    fr[b].remove(a)
    for j in range(N):
        if used[j] != -1:
            continue
        li = [j]
        used[j] = index
        dfs(fr,j,-1,index,li)
        index += 1
        renketu.append(li)
    if len(renketu) != 1:
        cnt += 1
    fr[a].append(b)
    fr[b].append(a)
print(cnt)