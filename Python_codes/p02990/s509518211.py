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
    if n - r < 0: return 0
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

def mcomb(n, k, mod):
    def mfac(l, r, mod):
        ans = l
        for i in reversed(range(r, l)):
            ans *= i
            ans %= mod
        return ans

    A = mfac(n, n-k+1, mod)
    B = mfac(k, 1, mod)
    # B = mpow(B,mod-2,mod)
    B = pow(B, mod-2, mod)
    return A * B % mod

def solve():
    N, K = MI()
    MOD = 1000000007
    aka = N - K
    for k in range(1, K+1):
        # ans = comb(aka+1, k) * comb(K-1, k-1)
        # print(comb(aka+1, k), comb(K-1, k-1))
        # print(aka+1, k, K-1, k-1)
        if aka+1 < k:
            a = 0
        else:
            a = mcomb(aka+1, k, MOD)
        if k-1 == 0:
            b = 1
        else:
            b = mcomb(K-1, k-1, MOD)
        # print(a, b)
        print(a * b % MOD)


if __name__ == '__main__':
    solve()
