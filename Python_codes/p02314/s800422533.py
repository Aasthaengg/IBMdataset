def solve(n, m, c):
    dp = [0] + [float("inf")] * n
    for i in range(1, n + 1):
        added_val = float("inf")
        for coin in c:
            added_val = min(added_val, dp[i - coin]) if 0 <= i - coin else added_val
        dp[i] = min(dp[i], added_val + 1)
    print(dp[n])

if __name__ == "__main__":
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    solve(n, m, c)
