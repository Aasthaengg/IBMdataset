N, M = map(int, input().split())
*S, = map(int, input().split())
*T, = map(int, input().split())

dp = [[0]*(M+1) for _ in range(N+1)]
accum = [[0]*(M+1) for _ in range(N+1)]
MOD = 10**9+7

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = 0 if S[i-1]!=T[j-1] else (1 + accum[i-1][j-1])%MOD
        accum[i][j] = (accum[i-1][j]+accum[i][j-1]-accum[i-1][j-1]+dp[i][j])%MOD     

ans = (sum(map(sum, dp))+1)%MOD
print(ans)
