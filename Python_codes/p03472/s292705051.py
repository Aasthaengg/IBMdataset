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
from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N, H = MI()
    A = [0] * N
    B = [0] * N
    amax = 0
    for i in range(N):
        a, b = MI()
        A[i] = a
        B[i] = b
        amax = max(amax, a)

    B_left = []
    for b in B:
        if amax < b:
            B_left.append(b)

    B_left = sorted(B_left, reverse=True)
    if len(B_left) > 0:
        ans = 0
        for i, b in enumerate(B_left):
            H -= b
            ans += 1
            if H <= 0:
                break
        if H > 0:
            ans += ceil(H / amax)
    else:
        ans = ceil(H / amax)
    print(ans)

if __name__ == '__main__':
    solve()