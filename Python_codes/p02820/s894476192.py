N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=input()

ans=0
for k in range(K):
    dp=[0,0,0]
    for i in range(k,N,K):
        #print(i)
        x=T[i]
        if x=='r':
            r,s,p=max(dp[1],dp[2]),max(dp[0],dp[2]),max(dp[0],dp[1])+P
        elif x=='s':
            r,s,p=max(dp[1],dp[2])+R,max(dp[0],dp[2]),max(dp[0],dp[1])
        else:
            r,s,p=max(dp[1],dp[2]),max(dp[0],dp[2])+S,max(dp[0],dp[1])
        dp=[r,s,p]
    ans+=max(dp)
print(ans)