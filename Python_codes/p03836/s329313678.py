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
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    sx, sy, tx, ty = MI()

    ans = deque([])
    # path1
    ans.extend(['U']*abs(ty - sy))
    ans.extend(['R']*abs(tx - sx))

    # path2
    ans.extend(['D']*abs(ty - sy))
    ans.extend(['L']*abs(tx - sx))

    # path3
    ans.extend(['L'])
    ans.extend(['U']*(abs(ty - sy)+1))
    ans.extend(['R']*(abs(tx - sx)+1))
    ans.extend(['D'])

    # path4
    ans.extend(['R'])
    ans.extend(['D'] * (abs(ty - sy)+1))
    ans.extend(['L'] * (abs(tx - sx)+1))
    ans.extend(['U'])

    # print(ans)
    printlist(ans, '')


if __name__ == '__main__':
    solve()
