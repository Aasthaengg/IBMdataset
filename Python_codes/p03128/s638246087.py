n, m = map(int, input().split())
a = list(map(int , input().split()))
t = [2,5,5,4,5,6,3,7,6]
cost = {ai: t[ai-1] for ai in a}

dp = [0] + [-1] * n

for i in range(1, n+1):
    dpi = -1
    for ai, ci in cost.items():
        if i - ci >= 0 and dp[i-ci] >= 0:
            dpi = max(dp[i-ci] * 10 + ai, dpi)
    dp[i] = dpi
print(dp[n])
