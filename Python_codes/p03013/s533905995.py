N, M = map(int, input().split())
dp = [0 for _ in range(N+1)]
skip = {}

for _ in range(M):
    skip[int(input())] = 1

dp[0] = 1
if 1 not in skip:
    dp[1] = 1

for i in range(2, N+1):
    if i in skip:
        continue
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

print(dp[N])
