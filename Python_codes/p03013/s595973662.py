N,M=map(int,input().split())
a=[int(input()) for _ in range(M)]

MOD=10**9+7

if N>1:
    dp=[0]*(N+1)
    dp[0]=1
    dp[1]=1

    for i in range(M):
        dp[a[i]]=-1

    for i in range(2,N+1):
        if dp[i]==-1:
            continue

        if dp[i-2]!=-1:
            dp[i]+=dp[i-2]
        
        if dp[i-1]!=-1:
            dp[i]+=dp[i-1]
        
        dp[i]=dp[i]%MOD

    print(dp[N])

else:
    if M==0:
        print(1)
    else:
        print(0)