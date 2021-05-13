import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
#from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
import math

#inf = 10**17
#mod = 10**9 + 7

n = int(input())
a = list(map(int, input().split()))
a.sort()
res = 0
for i in range(n, 3*n, 2):
    res += a[i]
print(res)