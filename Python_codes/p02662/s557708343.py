import sys
input=sys.stdin.readline


def main():
    N, S = map(int, input().split())
    *A, = map(int, input().split())
    dp = [[0]*(3001) for _ in range(N+1)]
    MOD = 998244353
    m = pow(2, MOD-2, MOD)
    dp[0][0] = pow(2, N, MOD)
    for i in range(1, N+1):    
        for j in range(3001):
            dp[i][j] += dp[i-1][j]
            if j-A[i-1]>=0:
                dp[i][j] += dp[i-1][j-A[i-1]]*m
            dp[i][j] %= MOD

    print(dp[N][S])


main()