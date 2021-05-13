def chmin(a, b):
    if a > b:
        return b
    return a
def resolve():
    n = int(input())
    h = list(map(int, input().split()))
    dp = [10**10] * n
    dp[0] = 0
    for i in range(n):
        dp[i] = chmin(dp[i], dp[i-1]+abs(h[i]-h[i-1]))
        if i > 1:
            dp[i] = chmin(dp[i], dp[i-2]+abs(h[i]-h[i-2]))
    print(dp[-1])
resolve()