#!python3

LI = lambda: list(map(int, input().split()))

# input
N, M = LI()
S = LI()
T = LI()

MOD = 10 ** 9 + 7


def main():
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
            dp[i][j] %= MOD
            if S[i - 1] == T[j - 1]:
                x = 1 + dp[i - 1][j - 1]
                dp[i][j] = (dp[i][j] + x) % MOD
    
    ans = (dp[-1][-1] + 1) % MOD
    print(ans)


if __name__ == "__main__":
    main()
