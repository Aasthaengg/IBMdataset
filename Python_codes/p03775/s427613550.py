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

import string

def main():
    N = i_input()

    l = []
    for i in range(1,math.ceil(sqrt(N))+1):
        if N % i == 0:
            l.append(i)

    ans = INF
    for i in l:
        b = N//i
        c = max(i,b)
        ans = min(ans, len(str(c)))
    print(ans)


if __name__=="__main__":
    main()
