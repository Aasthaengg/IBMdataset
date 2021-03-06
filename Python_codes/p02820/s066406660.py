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
    n,k = i_map()
    r,s,p = i_map()
    dic = {"r":p,"s":r,"p":s}
    t = list(s_input())
    ans = 0

    for i,j in enumerate(t):
        if i < k:
            ans += dic[j]
        else:
            if j != t[i-k]:
                ans += dic[j]
            else:
                t[i] = "z"
    print(ans)



if __name__=="__main__":
    main()
