N, M = map(int, input().split())
a = [0] * M
for i in range(M):
    a[i] = int(input())
a.append(N+1)
mod = 1000000007

dp = [0] * (N + 1)
dp[0] = 1
if a[0] == 1:
    a.pop(0)
else:
    dp[1] = 1

for i in range(2, N + 1):
    if a[0] == i:
        dp[i] = 0
        a.pop(0)
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[N])
