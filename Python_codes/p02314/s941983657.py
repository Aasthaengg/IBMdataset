n, m = map(int, input().split())
C = list(map(int, input().split()))

def coin():
    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for i in range(m):
        for j in range(C[i], n+1):
            dp[j] = min(dp[j], dp[j-C[i]]+1)
    return dp[n]

print(coin())

