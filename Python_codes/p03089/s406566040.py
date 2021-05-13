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
from collections import deque
from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations, islice
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N = II()
    B = deque(LI())
    B.appendleft(0)
    # print(B)
    ans = deque([])
    for i in range(N, 0, -1):
        tmp = deque([])
        # print(B)
        for j in range(i, 0, -1):
            # print(i, j, B[j])
            if B[j] == j:
                # print(tmp)
                tmp2 = deque(islice(B, 0, j))
                tmp2.extend(tmp)
                # print(tmp2)
                # tmp2.appendleft(0)
                B = tmp2
                ans.appendleft(j)
                break
            else:
                tmp.appendleft(B[j])
        else:
            print(-1)
            return

    printlist(list(ans), '\n')

if __name__ == '__main__':
    solve()
