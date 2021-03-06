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
    h,w = i_map()
    l = []
    for i in range(h):
        a = input()
        if "#" in a:
            l.append(a)
    l = [list(i) for i in zip(*l)]
    ans = []

    for i in l:
        if "#" in i:
            ans.append(i)

    ans = [i for i in zip(*ans)]
    for i in ans:
        print("".join(i))





if __name__=="__main__":
    main()
