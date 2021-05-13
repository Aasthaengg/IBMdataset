N,K=map(int,input().split())
h_list=list(map(int,input().split()))
dp=[0]*N
for i in range(1,N):
    dp[i]=float("inf")
    for j in range(1,min(i,K)+1):
        dp[i]=min(dp[i],dp[i-j]+abs(h_list[i-j]-h_list[i]))
print(dp[-1])