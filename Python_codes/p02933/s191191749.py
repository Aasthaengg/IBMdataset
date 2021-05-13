import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
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
a = int(input())
s = input()
if a >= 3200:
    print(s)
else:
    print("red")