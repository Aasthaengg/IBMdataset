
INF = 10**10

def main():
    s = input()
    N = len(s)
    s = '#' + s
    dp = [[(-INF) for j in range(3)] for i in range(N+1)]

    if len(s) == 1:
        print(1)
        exit()

    dp[0][1] = 0
    dp[0][2] = 0
    dp[1][1] = 1

    for i in range(2, N+1):
        # 1文字→1文字
        if s[i-1] != s[i]:
            dp[i][1] = max(dp[i][1], dp[i-1][1] + 1)
        
        # 2文字→1文字
        dp[i][1] = max(dp[i][1], dp[i-1][2] + 1)

        # 1文字→2文字
        dp[i][2] = max(dp[i][2], dp[i-2][1] + 1)

        # 2文字→2文字
        if i >= 4 and s[i-3:i-1] != s[i-1:i+1]:
            dp[i][2] = max(dp[i][2], dp[i-2][2] + 1)

    print(max(dp[N][1], dp[N][2]))


if __name__ == "__main__":
    main()