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
    n,y = i_map()
    for m in range(0,n+1):
        for g in range(0,n-m+1):
            if 10000*m+5000*g+1000*(n-m-g) == y:
                print(m,g,n-m-g)
                exit()
    print(-1,-1,-1)



if __name__=="__main__":
    main()
