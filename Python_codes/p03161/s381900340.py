def jmp(h,k):
    n=len(h)
    dp=[1000000000 for i in range(n+1)]
    dp[0]=0
    dp[1]=abs(h[1]-h[0])
    for i in range(n+1):
        for j in range(i+1,i+k+1):
            if(j<n):
                dp[j]=min(dp[j],dp[i]+abs(h[i]-h[j]))
    # print(dp)
    return dp[n-1]
 
 
n,k=map(int,input().split())
l=list(map(int,input().split()))
print(jmp(l,k))