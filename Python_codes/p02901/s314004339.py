from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


def main():
    N, M = map(int, input().split())
    
    key_price = [0]*M
    key_bit = [0]*M
    for i in range(M):
        key_price[i], b = map(int, input().split())
        c = list(map(int, input().split()))
        for j in range(b):
            key_bit[i] = key_bit[i] | (1 << (c[j] - 1))
    
    dp = [[INF] * (2**N) for _ in range(M+1)]
    dp[0][0] = 0
    for m in range(M):
        for bit in range(2**N):
            if dp[m][bit] == INF:
                continue
            dp[m+1][bit] = min(dp[m+1][bit], dp[m][bit])
            dp[m+1][bit | key_bit[m]] = min(dp[m+1][bit | key_bit[m]], dp[m][bit] + key_price[m])

    res = dp[M][2**N-1]
    if res == INF:
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    main()