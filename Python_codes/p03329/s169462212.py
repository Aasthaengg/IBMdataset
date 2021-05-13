N = int(input())

dp = list(range(0, N+1))

for i in range(1, N+1):
    for j in [6, 9]:
        for k in range(1, N):
            if 0 <= i-j**k:
                dp[i] = min(dp[i], dp[i-j**k]+1)
            else:
                break

print(dp[-1]) 