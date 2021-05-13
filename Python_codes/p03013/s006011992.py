MOD = 10**9+7
N, M = map(int, input().split())
N += 1
A = set()
for _ in range(M):
    A.add(int(input()))
dp = [0]*N
dp[0] = 1
if 1 not in A:
    dp[1] = 1
for i in range(2,N):
    if i not in A:
        dp[i] += dp[i-1] + dp[i-2]
        dp[i] %=MOD
print(dp[-1])