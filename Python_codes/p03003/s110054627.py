def main():

    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    mod = pow(10, 9) + 7
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    dp[0][0] = 0
    # for i in range(N): dp[i][0] = 0
    # for j in range(M): dp[0][j] = 0

    for i in range(N):
        for j in range(M):
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] - dp[i][j]
            if S[i] == T[j]:
                dp[i+1][j+1] += dp[i][j] + 1
            dp[i+1][j+1] %= mod
    # print(dp)
    return dp[N][M] + 1

if __name__ == '__main__':
    print(main())
