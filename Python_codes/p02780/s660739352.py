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
    n, k = i_map()
    p = i_list()


    sowa = [0]
    for i in range(1,1001):
        sowa.append(sowa[i-1]+i)

    l = [sowa[p[0]]/p[0]]

    for i in range(1,n):
        l.append(l[i-1] + sowa[p[i]]/p[i])


    ans = l[k-1]
    for i in range(k,n):
        s = l[i] - l[i-k]
        ans = max(ans,s)
    print(ans)


if __name__=="__main__":
    main()
