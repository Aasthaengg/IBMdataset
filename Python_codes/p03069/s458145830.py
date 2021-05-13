from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
from collections import Counter, deque, defaultdict

N = int(input())
S = input()

mi = 10000000

c = Counter(S)
A = N - c["#"]
B = N - c["."]

l = 0
r = c["."]

for i in range(0, N):

    if S[i] == "#":
        l += 1
    else:
        r -= 1
    a = l + r
    if mi > a:
        mi = a

print(min(mi, A, B))