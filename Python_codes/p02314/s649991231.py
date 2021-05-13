def main():
    n, m = list(map(int, input().split()))
    coins = list(map(int, input().split()))

    dp = [float('inf')] * 50001
    dp[0] = 0

    for i in range(m):
        for j in range(n+1):
            if j + coins[i] > n:
                break
            else:
                dp[j + coins[i]] = min(dp[j + coins[i]], dp[j] + 1)

    print(dp[n])
main()

