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
# from collections import deque, defaultdict
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def mcomb(n, k, mod):
    if k == 0: return 1     # １分割の場合は１を返すようにしておく
    def mfac(l, r, mod):
        ans = l
        for i in reversed(range(r, l)):
            ans *= i
            ans %= mod
        return ans

    A = mfac(n, n - k + 1, mod)
    B = mfac(k, 1, mod)
    # B = mpow(B,mod-2,mod)
    B = pow(B, mod - 2, mod)
    return A * B % mod

def solve():
    S = II()
    ans = 0
    MOD = 1000000007
    for n in range(1, S//3+1):
        # print(n)
        # print(mcomb(S-3*n+n-1, n-1, MOD))
        ans += mcomb(S-3*n+n-1, n-1, MOD)
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    solve()

