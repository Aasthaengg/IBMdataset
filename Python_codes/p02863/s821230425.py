N,T = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]
AB.sort()

dp = [0]*(T)
ans = 0
for a,b in AB:
    ans = max(ans,dp[-1]+b)
    for i in range(T-1,-1,-1):
        if i-a >= 0:
            dp[i] = max(dp[i],dp[i-a]+b)
print(ans)
