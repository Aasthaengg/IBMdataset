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
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N = II()
    A = LI()
    A.sort()

    sm = 0
    j = -1
    for i, a in enumerate(A[:-1]):
        sm += a
        # print(sm, 2 * sm, A[i+1])
        if 2 * sm >= A[i+1]:
            pass
        else:
            j = i
    # print(j)
    print(N - (j + 1))

if __name__ == '__main__':
    solve()
