# Begin Header {{{
from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
# }}} End Header
# _________コーディングはここから！！___________
t = defaultdict(int)
n, m = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    t[a]+=1
    t[b]+=1
for j in range(1, n+1):
    print(t[j])