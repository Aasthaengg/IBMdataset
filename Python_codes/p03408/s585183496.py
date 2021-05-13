# Begin Header {{{
from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
# }}} End Header
# _________コーディングはここから！！___________
# ... 最小側の制約も確認した？
# ... オーバーフローしない？
n = int(input())
blue = [input() for i in range(n)]
k = int(input())
red = [input() for i in range(k)]
T={}
for x in blue:
    if x not in T: T[x] = 1
    else: T[x]+=1
for x in red:
    if x not in T: T[x] = -1
    else: T[x]-=1
print(max(max(T.values()), 0))