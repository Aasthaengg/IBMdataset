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
    sx,sy,ex,ey = i_map()

    fp = "U"*(ey-sy)
    fr = "R"*(ex-sx)
    fd = "D"*(ey-sy)
    fl = "L"*(ex-sx)
    f = fp+fr+fd+fl

    fl = "L"
    sp = "U"*(ey-sy+1)
    fr = "R"*(ex-sx+1)
    fd = "D"
    sr = "R"
    sd = "D"*(ey-sy+1)
    sl = "L"*(ex-sx+1)
    p = "U"
    s = fl+sp+fr+fd+sr+sd+sl+p

    print(f+s)











if __name__=="__main__":
    main()
