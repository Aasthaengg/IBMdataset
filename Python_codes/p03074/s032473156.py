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
N,K = map(int,input().split())
S = list(input())[:-1]
def rle(s):#計算量N
    n = len(s)
    tmp, count,stt,end = s[0], 1,[],[]
    for i in range(1,len(s)):
        if tmp == s[i]:
            count += 1
        else:
            if tmp == "1":
                stt.append(i-count)
                end.append(i-1)
            tmp = s[i]
            count = 1
    if s[n-1] == "1":
        stt.append(n-count)
        end.append(n-1)
    return stt,end #最大2N文字
stt,end = rle(S)
n = len(stt)
if S[0] == "1" and S[N-1] == "1":
    if K >= n-1:
        print(N)
    else:
        MAX = 0
        for i in range(n-K):
            MAX = max(MAX,end[i+K]-stt[i]+1)
        print(MAX)
elif S[0] == "0" and S[N-1] == "0":
    if K >= n+1:
        print(N)
    else:
        MAX = max(end[K-1]+1,N-stt[-K])
        for i in range(n-K):
            MAX = max(MAX,end[i+K]-stt[i]+1)
        print(MAX)
elif S[0] == "1" and S[N-1] == "0":
    if K >= n:
        print(N)
    else:
        MAX = N-stt[-K]
        for i in range(n-K):
            MAX = max(MAX,end[i+K]-stt[i]+1)
        print(MAX)
else:
    if K >= n:
        print(N)
    else:
        MAX = end[K-1]+1
        for i in range(n-K):
            MAX = max(MAX,end[i+K]-stt[i]+1)
        print(MAX)