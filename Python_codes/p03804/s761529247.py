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
    N,M = i_map()
    a = [s_input() for _ in range(N)]
    b = [s_input() for _ in range(M)]

    for i in range(N-M+1):
        for j in range(N-M+1):
            flg = True

            for x in range(M):
                for y in range(M):
                    if b[x][y] != a[i+x][j+y]:
                        flg = False
                        break
                if flg == False:
                    break
            if flg == True:
                print("Yes")
                exit()
    print("No")

if __name__=="__main__":
    main()
