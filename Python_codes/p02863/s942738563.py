"""
食べるのにかかる時間順にソートしてナップサックするのがよい。
dp[i][j]
"""
N,T = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[0])
dp = [[0]*(T) for _ in range(N+1)]
for i in range(1,N+1):
    a,b = AB[i-1]
    for j in range(1,T):
        if j-a >= 0:
            dp[i][j] = max(dp[i-1][j-a]+b,dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

ans = 0
for i in range(1,N):
    a,b = AB[i]
    ans = max(ans,dp[i][-1]+b)
print(ans)