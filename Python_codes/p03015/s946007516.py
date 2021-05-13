def main():
    L = input().rstrip()
    MOD = 10**9 + 7
    dp = [[0 for equal in range(2)] for digit in range(len(L) + 1)]
    dp[0][0] = 1
    for digit in range(len(L)):
        x = int(L[digit])
        if x == 1:
            dp[digit+1][1] += dp[digit][0] + dp[digit][1]
            dp[digit+1][0] += dp[digit][0] * 2
            dp[digit+1][1] += dp[digit][1] * 2
        else:
            dp[digit+1][0] += dp[digit][0]
            dp[digit+1][1] += dp[digit][1]
            dp[digit+1][1] += dp[digit][1] * 2
        dp[digit+1][0] %= MOD
        dp[digit+1][1] %= MOD
    print((dp[len(L)][0] + dp[len(L)][1])%MOD)

if __name__ == "__main__":
    main()