from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
INF = float("inf")
MOD = 998244353



# 処理内容
def main():
    N, K = map(int, input().split())
    
    L = [0]*K
    R = [0]*K
    for i in range(K):
        L[i], R[i] = map(int, input().split())

    dp = [0]*(N*2 + 1)
    a = [0]*(N*2 + 1)
    dp[0] = 1
    a[1] = -1
    for i in range(N):
        for j in range(K):
            a[i+L[j]] += dp[i]
            a[i+R[j]+1] -= dp[i]
        dp[i+1] = (dp[i] + a[i+1]) % MOD
    
    print(dp[N-1])



if __name__ == '__main__':
    main()