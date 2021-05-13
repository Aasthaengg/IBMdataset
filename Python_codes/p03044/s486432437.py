import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
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
import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    u,v,w = map(int,(input().split()))
    tree[u-1].append((v-1,w))
    tree[v-1].append((u-1,w))
color = [-1]*N
black = 0
white = 1
color[0] = white
def dfs(cur,parent):
    li = tree[cur]
    for chi,dis in li:
        if chi == parent:
            continue
        if dis % 2 == 0:
            color[chi] = color[cur]
            dfs(chi,cur)
        else:
            if color[cur] == black:
                color[chi] = white
            else:
                color[chi] = black
            dfs(chi,cur)
dfs(0,-1)
for i in color:
    print(i)