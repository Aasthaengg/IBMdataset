def solve(string):
    s = string.replace("?", "d").lower()
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(4)]
    dp[0][0] = 1
    mod = 10**9 + 7
    for i, _s in enumerate(s):
        dp[0][i + 1] = dp[0][i] % mod
        dp[1][i + 1] = dp[1][i] % mod
        dp[2][i + 1] = dp[2][i] % mod
        dp[3][i + 1] = dp[3][i] % mod
        if _s == "a":
            dp[1][i + 1] += dp[0][i]
        if _s == "b":
            dp[2][i + 1] += dp[1][i]
        if _s == "c":
            dp[3][i + 1] += dp[2][i]
        if _s == "d":
            dp[0][i + 1] *= 3
            dp[1][i + 1] *= 3
            dp[1][i + 1] += dp[0][i]
            dp[2][i + 1] *= 3
            dp[2][i + 1] += dp[1][i]
            dp[3][i + 1] *= 3
            dp[3][i + 1] += dp[2][i]
    return str(int(dp[3][-1] % (10**9 + 7)))


if __name__ == '__main__':
    print(solve(input()))
