N = int(input())
c = [1]
temp = 6
while(temp <= N):
    c.append(temp)
    temp *= 6
temp = 9
while(temp <= N):
    c.append(temp)
    temp *= 9
m = len(c)

dp = [10 ** 9 + 7 for _ in range(N + 1)]
dp[0] = 0
for i in range(m):
    for j in range(1, N + 1):
        if j - c[i] >= 0:
            dp[j] = min(dp[j], dp[j - c[i]] + 1)
print(dp[N])