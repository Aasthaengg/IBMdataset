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

def prime_factorization(n):
    res = []
    for i in range(2, int(pow(n, 0.5))+1):
        if n % i: continue
        ex = 0
        while n % i == 0:
            n = n // i
            ex += 1
        res.append((i, ex))
    if n != 1:
        res.append((n, 1))
    return res

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
    N, M = MI()
    fact = prime_factorization(M)
    MOD = 1000000007

    if N == 1:
        print(1)
        return

    ans = 1
    for num, ex in fact:
        ans = ans * mcomb(ex+N-1, N-1, MOD)
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    solve()
