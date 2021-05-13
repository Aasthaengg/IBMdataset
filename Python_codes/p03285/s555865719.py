n = int(input())

dp = [False] * (n + 1)
dp[0] = True
for i in range(n-3):
    if dp[i]:
        dp[i+4] = True
for i in range(n-6):
    if dp[i]:
        dp[i+7] = True

if dp[n]:
    print('Yes')
else:
    print('No')