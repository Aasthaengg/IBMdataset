N = int(input())

i = 1
cash = []
while i <= N:
    cash.append(i)
    i *= 6
i = 9
while i <= N:
    cash.append(i)
    i *= 9

dp = [10**6+10] * (N+1)
dp[0] = 0
for i in range(1, N+1):
    for j in cash:
        if i-j >= 0:
            dp[i] = min(dp[i], dp[i-j]+1)
print(dp[-1])