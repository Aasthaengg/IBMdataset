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
    sx, sy, tx, ty = MI()

    ans = ''
    # path1
    ans += 'U' * abs(ty - sy) + 'R' * abs(tx - sx)

    # path2
    ans += 'D' * abs(ty - sy) + 'L' * abs(tx - sx)

    # path3
    ans += 'L' + 'U' * (abs(ty - sy) + 1) + 'R' * (abs(tx - sx) + 1) + 'D'

    # path4
    ans += 'R' + 'D' * (abs(ty - sy) + 1) + 'L' * (abs(tx - sx) + 1) + 'U'

    print(ans)

if __name__ == '__main__':
    solve()
