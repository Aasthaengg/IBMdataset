import sys
if __name__ == "__main__":
    n = int(input())
    if n == 0 or n == 1:
        print(1)
        sys.exit(0)
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])