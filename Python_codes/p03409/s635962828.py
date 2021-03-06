import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7

import sys
sys.setrecursionlimit(10**6)
import itertools
import bisect
from collections import Counter,deque
def i_input(): return int(input())
def i_map(): return map(int, input().split())
def i_list(): return list(i_map())
def i_row(N): return [i_input() for _ in range(N)]
def i_row_list(N): return [i_list() for _ in range(N)]
def s_input(): return input()
def s_map(): return input().split()
def s_list(): return list(s_map())
def s_row(N): return [s_input for _ in range(N)]
def s_row_str(N): return [s_list() for _ in range(N)]
def s_row_list(N): return [list(s_input()) for _ in range(N)]


def main():
    n = i_input()
    R = sorted([i_list() for _ in range(n)])
    B = sorted([i_list() for _ in range(n)])

    ans = 0
    for bx, by in B:
        C = [(y,x) for x,y in R if x<bx and y < by]
        if len(C) == 0:
            continue
        ans += 1
        C.sort(reverse=True)
        R.remove([C[0][1],C[0][0]])
    print(ans)


if __name__=="__main__":
    main()
