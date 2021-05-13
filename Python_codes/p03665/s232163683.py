import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')
# from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate

def comb(n, r):
    # if n - r < 0: return 0
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def solve():
    N, P = MI()
    A = LI()

    cnt = {}
    for a in A:
        cnt[a % 2] = cnt.get(a%2, 0) + 1
    # print(cnt)

    ans = 0

    one = cnt.get(1, 0)
    zero = cnt.get(0, 0)
    if P == 0:
        for i in range(0, one+1, 2):
            # print(i)
            # print(comb(one, i))
            ans += comb(one, i)

        print(ans * (pow(2, zero)))
    else:
        for i in range(1, one+1, 2):
            ans += comb(one, i)
        print(ans * pow(2, zero))


if __name__ == '__main__':
    solve()
