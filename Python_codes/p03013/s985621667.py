N, M = map(int, input().split())
dp = [0 for _ in range(N+1)]
skip = {}

for _ in range(M):
    skip[int(input())] = 1

dp[1] = 1
if N >= 2:
    dp[2] = 2

if 1 in skip:
    dp[1] = 0
    if N >= 2:
        dp[2] = 1
if 2 in skip:
    if N >= 2:
        dp[2] = 0

for i in range(3, N+1):
    if i in skip:
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[N])
