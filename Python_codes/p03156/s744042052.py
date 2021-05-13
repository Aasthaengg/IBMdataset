# Begin Header {{{
from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
# }}} End Header
# _________コーディングはここから！！___________
n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
k=0
l=0
m=0
for x in p:
    if x<=a: k+=1
    elif x>=a+1 and x<=b: l+=1
    elif x>=b+1: m+=1
print(min(k, l, m))
