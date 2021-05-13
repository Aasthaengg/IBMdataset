N,M = map(int,input().split())
oks = [True]*(N+1)
for i in range(M):
   a = int(input())
   oks[a] = False
dp = [0]*(N+1)
dp[0] = 1
mod = 1000000007
for now in range(N):
    for next in range(now+1,min(N,now+2)+1): #1段または2段すすむ。際集団を超えないように
        if oks[next]: #階段が壊れていなければ
            dp[next] += dp[now]
            dp[next] %= mod
print(dp[N])
