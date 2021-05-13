import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    n,m = map(int, input().split())
    dp = [0]*(n+1)
    dp[0] = 1
    a = [int(input()) for _ in range(m)]
    b = [1]*(n+1)

    for i in range(m):
        b[a[i]] = 0
    for i in range(n):
        if i - 1 >= 0:
            dp[i+1] = dp[i]*b[i]+dp[i-1]*b[i-1]
        else:
            dp[i+1] = dp[i]*b[i]
        dp[i+1] %= 10**9+7
    print(dp[n])

if __name__=="__main__":
    main()
