N,K=map(int,input().split())
H=list(map(int,input().split()))

dp=[float('inf')]*N
dp[0]=0
dp[1]=abs(H[1]-H[0])

for n in range(2,N):
    if n-K>0:
        dp[n]=min([(dp[i]+abs(H[n]-H[i]))for i in range(n-K,n)])
    else:
        dp[n]=min([dp[i]+abs(H[n]-H[i])for i in range(0,n)])

print(dp[N-1])