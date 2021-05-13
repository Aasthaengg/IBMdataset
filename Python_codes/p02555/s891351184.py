def main():
    total = int(input())
    mod = 1000000007
    dp = [0] * (total + 1)
    dp[0] = 1
    for i in range(1, total + 1):
        right = max(0, i - 3 + 1)
        dp[i] = sum(dp[0: right]) % mod
    return dp[total]


if __name__ == '__main__':
    print(main())
