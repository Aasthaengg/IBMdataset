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
M,K = map(int,input().split())
if M == 1:
    if K == 0:
        ans = [0,0,1,1]
        print(*ans)
    else:
        print(-1)
else:
    if K > 2**M - 1 :
        print(-1)
    else:
        if K == 0:
            ans = []
            for i in range(2**M):
                ans.append(i)
                ans.append(i)
            print(*ans)
        else:
            ans = deque([K])
            for i in range(2**M):
                if i == K:
                    continue
                ans.append(i)
                ans.appendleft(i)
            ans.append(K)
            print(*ans)