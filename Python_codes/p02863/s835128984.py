n,t=map(int,input().split())
info=[tuple(reversed(list(map(int,input().split())))) for i in range(n)]

#(美味しさ,頼まなかったやつの美味しさ最大値)
dp=[(-10**9,-10**9)]*t
dp[0]=(0,0)

for _ in reversed(sorted(info)):
    good,time=_
    for i in range(t-1,-1,-1):
        g0,m0=dp[i]
        dp[i]=(g0,max(m0,good))
        if i>=time:
            g1,m1=dp[i-time]
            if g0+m0<g1+good+m1:
                dp[i]=(g1+good,m1)
ans=0
for a,b in dp:
    ans=max(ans,a+b)

print(ans)