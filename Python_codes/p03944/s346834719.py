import math
from math import gcd,pi,sqrt
INF = float("inf")

import sys
sys.setrecursionlimit(10**6)
import itertools
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
    w,h,n = i_map()

    up = h
    right = w
    down = 0
    left = 0

    for i in range(n):
        x,y,a = i_map()
        if a == 1:
            left = max(left,x)
        elif a == 2:
            right = min(right, x)
        elif a == 3:
            down = max(down, y)
        else:
            up = min(up, y)
    print(max((up-down),0)*max((right-left),0))

if __name__=="__main__":
    main()
