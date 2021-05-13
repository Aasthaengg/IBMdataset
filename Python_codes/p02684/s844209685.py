#! /usr/bin/env python3

from fractions import gcd
# from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement

N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]

flag = 0
done = [0] * (N + 1)

root = []
ind = 0

ind = A[0]
root = [1]
done[1] = 1

while True:

    if done[ind]:
        flag = 1
        break
    done[ind] = 1

    root += [ind]
    ind = A[ind-1]

if flag:
    if len(root) <= K:
        left = root.index(ind) - 1
        loopcnt = len(root) - (root.index(ind))

        root2 = root[left+1:]
        print(root2[(K-(left+1)) % loopcnt])
    else:
        print(root[K])
else:
    print(root[K-1])
