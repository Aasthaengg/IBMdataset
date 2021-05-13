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
alf = list("abcdefghijklmnopqrstuvwxyz")
ALF = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
#import numpy as np
INF = float("inf")
#d = defaultdict(int)
#d = defaultdict(list)
#N = int(input())
#A = list(map(int,input().split()))
#S = list(input())[:-1]
#S.remove("\n")
#N,M = map(int,input().split())
#S,T = map(str,input().split())
#A = [int(input()) for _ in range(N)]
#S = [list(input())[:-1] for _ in range(N)]
#A = [list(map(int,input().split())) for _ in range(N)]
n = int(input())
a = n % 10
n //= 10
b = n % 10
n //= 10
c = n % 10
n //= 10
d = n % 10
if a == b or b == c or c == d:
    print("Bad")
else:
    print("Good")