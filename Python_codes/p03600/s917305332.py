import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import math
#from collections import defaultdict
#d = defaultdict(int)
#import fractions
#import math
#import collections
#from collections import deque
#from bisect import bisect_left
#from bisect import insort_left
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [input() for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
#import itertools
#import heapq
#import numpy as np
#INF = float("inf")
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
flag = 1
s = 0
for i in range(N-1):
    if flag == 0:
        break
    for j in range(i+1,N):
        judge = 1
        if flag == 0:
            break
        a = A[i][j]
        s += a
        for k in range(N):
            if k == i or k == j:
                continue
            elif a > A[i][k] + A[k][j]:
                flag = 0
                break
            elif a == A[i][k] + A[k][j]:
                s -= a
                break
            else:
                continue
if flag == 0:
    print(-1)
else:
    print(s)