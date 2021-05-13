def solve(k, a):
    dp = [False]*(k+1)
    for i in range(1, k+1):
        for x in a:
            if i - x >= 0:
                dp[i] = dp[i] or not dp[i-x]
    return dp[-1]

n, k = map(int, input().split())
a = list(map(int, input().split()))
print('First' if solve(k, a) else 'Second')