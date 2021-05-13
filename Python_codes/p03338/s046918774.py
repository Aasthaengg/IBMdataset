from fractions import gcd
# from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement

n = int(input())
s = input()
ans = 0
for i in range(1,n):
    cnt = 0
    c1 = Counter(s[:i])
    c2 = Counter(s[i:])
    for x in c1.keys():
        if c2[x]: cnt+=1
    ans = max(cnt, ans)
print(ans)