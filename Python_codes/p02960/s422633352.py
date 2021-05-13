mod = 10**9+7
def main():
    s = list(input())
    n = len(s)
    dp = [[0 for _ in range(13)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n):
        if s[i] != '?':
            s[i] = int(s[i])
            for k in range(13):
                index = (k*10+s[i])%13
                dp[i+1][index] += dp[i][k]
        else:
            for j in range(10):
                for k in range(13):
                    index = (k*10+j)%13
                    dp[i+1][index] += dp[i][k]
        for j in range(13):
            dp[i+1][j] %= mod
    print(dp[n][5])

if __name__ == "__main__":
    main()