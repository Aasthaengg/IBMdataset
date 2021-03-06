def solve():
    S = input()
    N = len(S)
    MOD = 10 ** 9 + 7

    dp = [[0] * 13 for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(13):
            if S[i] != '?':
                dp[i+1][(10 * j + int(S[i])) % 13] += dp[i][j] % MOD
            else:
                for k in range(0,10):
                    dp[i+1][(10 * j + k) % 13] += dp[i][j] % MOD
    
    print(dp[-1][5] % MOD)

if __name__ == '__main__':
    solve()