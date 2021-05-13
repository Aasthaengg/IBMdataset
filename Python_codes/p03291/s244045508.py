def main():
    s = input()
    N = len(s)

    dp = [[-1]*4 for n in range(N)]
    for i in reversed(list(range(N))):
        for j in range(4):
            if i == N-1:
                if j == 3:
                    dp[i][j] = 3 if s[i] == "?" else 1
                elif j == 2:
                    dp[i][j] = 1 if s[i] in ("?", "C") else 0
                else:
                    dp[i][j] = 0
            else:
                if j == 3:
                    dp[i][j] = (3 if s[i] == "?" else 1) * dp[i+1][j]
                elif s[i] == "?":
                    dp[i][j] = 3 * dp[i+1][j] + dp[i+1][j+1]
                elif s[i] == "ABC"[j]:
                    dp[i][j] = dp[i+1][j+1] + dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
            dp[i][j] %= 10 ** 9 + 7
    print(dp[0][0])


if __name__ == "__main__":
    main()