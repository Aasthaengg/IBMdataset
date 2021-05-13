N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

ans=0
for i in range(K):
    tt=T[i:N:K]
    l=len(tt)
    dp = [[0]*l for _ in range(3)]
    if tt[0]=="r":
        dp[2][0]=P
    if tt[0]=="s":
        dp[0][0]=R
    if tt[0]=="p":
        dp[1][0]=S
    
    for i in range(1,l):
        if tt[i]=="r":
            dp[0][i] = max(dp[1][i-1],dp[2][i-1])
            dp[1][i] = max(dp[2][i-1],dp[0][i-1])
            dp[2][i] = max(dp[0][i-1],dp[1][i-1])+P
        if tt[i]=="s":
            dp[0][i] = max(dp[1][i-1],dp[2][i-1])+R
            dp[1][i] = max(dp[2][i-1],dp[0][i-1])
            dp[2][i] = max(dp[0][i-1],dp[1][i-1])
        if tt[i]=="p":
            dp[0][i] = max(dp[1][i-1],dp[2][i-1])
            dp[1][i] = max(dp[2][i-1],dp[0][i-1])+S
            dp[2][i] = max(dp[0][i-1],dp[1][i-1])
    ans+= max(dp[h][-1] for h in range(3))
print(ans)