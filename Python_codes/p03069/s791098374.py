from functools import reduce
from fractions import gcd
from collections import defaultdict
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


# 処理内容
def main():
    N = int(input())
    S = input()[:-1]

    l = 0
    r = 0
    for i in range(N):
        if S[i] == ".":
            r += 1
    
    ans = l + r
    for i in range(N):
        if S[i] == "#":
            l += 1
        else:
            r -= 1
        ans = min(ans, l + r)
    
    print(ans)
    


if __name__ == '__main__':
    main()