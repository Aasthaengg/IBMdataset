N, M = list(map(int, input().split()))
C = 10**9+7
S = set()
for _ in range(M):
    S.add(int(input()))
dp = [0]*(N+1)
dp[0] = 1
if not 1 in S:
    dp[1] = 1
for i in range(2, N+1):
    if i in S:
        continue
    dp[i] = (dp[i-1]+dp[i-2]) % C
print(dp[N])
