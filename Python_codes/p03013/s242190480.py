MOD = 10**9 + 7
N,M = map(int, input().split())
a = [int(input()) for _ in range(M)]

aa = [True] * (N+1)
for i in a:
    aa[i] = False

dp = [0] * (N+1)
dp[0] = 1
if aa[1]:
    dp[1] = 1

for i in range(2,N+1):
    if (aa[i] == False):
        dp[i] = 0
        continue
    dp[i] = dp[i-1] + dp[i-2]
    dp[i] =  dp[i] % MOD
print(dp[N])
