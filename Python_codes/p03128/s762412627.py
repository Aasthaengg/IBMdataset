n, m = map(int, input().split())
a = list(map(int , input().split()))
t = [2,5,5,4,5,6,3,7,6]
cost = {ai: t[ai-1] for ai in a}

dp = [0] + [-1] * n

for i in range(n+1):
    tmp = []
    for ai, ci in cost.items():
        if i - ci >= 0 and dp[i-ci] >= 0:
            tmp.append(dp[i-ci] * 10 + ai)
    if len(tmp) > 0:
        dp[i] = max(tmp)
print(dp[n])