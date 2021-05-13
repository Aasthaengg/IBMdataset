def solve():
    #start here
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [0 for i in range(n)]
    for i in range(1, n):
        x = float('inf')
        for j in range(1, 1 + min(k, i)):
            x = min(x, dp[i-j] + abs(h[i]-h[i-j]))
        dp[i] = x
    print(dp[n-1])

solve()