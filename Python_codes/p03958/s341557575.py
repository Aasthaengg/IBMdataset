'''
from math import gcd
from itertools import accumulate, combinations, permutations, product
from bisect import bisect, bisect_left
from collections import Counter, defaultdict, deque
from heapq import heappush, heappop
from functools import reduce
from operator import add, mul, sub, truediv, floordiv, mod

from decimal import *
getcontext().prec = 500

import string
ascii = string.ascii_lowercase
'''
from sys import stdin


def main():
    input = lambda: stdin.readline()[:-1]
    K, T = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort(reverse=1)
    cake = []
    x = []
    n = (K + 1) // 2
    for i in range(T):
        if A[i] > n:
            cake += [i] * n
            x += [i] * (A[i] - n)
        else:
            cake += [i] * A[i]
    cake += x
    turn = [0] * K
    j = 0
    for i in range(0, K, 2):
        turn[i] = cake[j]
        j += 1
    for i in range(1, K, 2):
        turn[i] = cake[j]
        j += 1
    ans = 0
    for i in range(1, K):
        ans += turn[i-1] == turn[i]
    print(ans)


main()
