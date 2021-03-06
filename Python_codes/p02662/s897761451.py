import sys
sys.setrecursionlimit(10000000)
MOD = 998244353
INF = 10 ** 15
import numpy as np

def main():
    N,S = map(int,input().split())
    A = list(map(int,input().split()))

    dp = np.zeros(S + 1,np.int64)
    dp[0] = pow(2,N,MOD)
    inv2 = pow(2,MOD - 2,MOD)
    for a in A:
        dp[a:] = np.mod(dp[a:] + dp[:-a] * inv2,MOD)
    print(dp[S])
if __name__ == '__main__':
    main()