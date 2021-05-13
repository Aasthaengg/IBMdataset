MOD = 10**9 + 7


def main():
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    dp = [[0] * (M+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = 1
    for i in range(M+1):
        dp[0][i] = 1
    ans = 1
    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                cur = dp[i][j]
            else:
                cur = 0
            dp[i+1][j+1] = (dp[i+1][j] + dp[i][j+1] +
                            - dp[i][j] + cur) % MOD
#    print(dp)
    print(dp[N][M])


if __name__ == "__main__":
    main()
