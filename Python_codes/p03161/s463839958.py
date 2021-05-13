N,K=map(int,input().split())
H=list(map(int,input().split()))



if N>K:
    dp=[1000000000]*N
    dp[0]=0
    for i in range(1,K):
        dp[i]=abs(H[i]-H[0])

    for i in range(K,N):
        for j in range(1,K+1):
            dp[i]=min(dp[i], dp[i-j]+abs(H[i-j]-H[i]))

    print(dp[N-1])

else:
    print(abs(H[N-1]-H[0]))