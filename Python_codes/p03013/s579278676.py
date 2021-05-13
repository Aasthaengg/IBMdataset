n, m = map(int, input().split())
set_A = set()
dp = [0]*n
mod = pow(10, 9) + 7

for _ in range(m):
    set_A.add(int(input()))

if 1 not in set_A:
    dp[0] = 1
if 2 not in set_A and n != 1:
    dp[1] = 1 + dp[0]

for i in range(2, n):
    if i + 1 not in set_A:
        dp[i] += (dp[i-1] + dp[i-2])%mod

print(dp[n-1])