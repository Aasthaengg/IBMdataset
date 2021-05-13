def main():
    MOD = 10 ** 9 + 7

    S = input()

    N = len(S)
    dp = [[0] * 4 for _ in range(N + 1)]

    for i in reversed(range(N + 1)):
        for j in reversed(range(4)):
            if i == N:
                dp[i][j] = int(j == 3)
            else:
                dp[i][j] = dp[i + 1][j] * (3 if S[i] == "?" else 1)
                if j < 3 and (S[i] == "?" or S[i] == "ABC"[j]):
                    dp[i][j] += dp[i + 1][j + 1]
                dp[i][j] %= MOD

    print(dp[0][0])


if __name__ == '__main__':
    main()
