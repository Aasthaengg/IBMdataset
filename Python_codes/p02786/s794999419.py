from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
input = sys.stdin.readline
INF = float("inf")


# 処理内容
def main():
    H = int(input())
    ans = 0
    i = 0
    while(H >= 1):
        ans += 2**i
        H /= 2
        i += 1

    print(ans)
    

if __name__ == '__main__':
    main()