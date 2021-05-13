N,M = map(int,input().split())
broken = set()
for i in range(M):
    broken.add(int(input()))
dp = [0 for i in range(N+1)]
dp[0] = 1
if 1 not in broken:
    dp[1] = 1
for i in range(2,N+1):
    if i in broken:
        dp[i] = 0
    else:
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1000000007
print(dp[N])