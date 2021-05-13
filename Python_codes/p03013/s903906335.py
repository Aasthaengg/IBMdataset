n, m = map(int, input().split())
bad = []
for i in range(m):
    bad.append(int(input()))
dp = [0 for x in range(n+1)]
dp[0] = 1
idx = 0
if m > 0 and bad[0] == 1:
    dp[1] = 0
    idx = 1
else:
    dp[1] = 1

for i in range(2, n+1):
    if idx < m and i == bad[idx]:
        dp[i] = 0
        idx+=1
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[n])



