N,K=map(int,input().split())
a=list(map(int,input().split()))
dp=[[0,0]  for j in range(K+1)]
for i in range(1,K+1):
    for j in range(N):
        if i-a[j]>=0:
            dp[i][0]=max((dp[i-a[j]][1]+1)%2,dp[i][0])
            dp[i][1]=max((dp[i-a[j]][0]+1)%2,dp[i][1])
        
if dp[K][0]:
    print("First")
else:
    print("Second")

