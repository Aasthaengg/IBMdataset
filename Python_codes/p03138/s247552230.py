N,K=map(int,input().split())
A=list(map(int,input().split()))
s=sum(A)
dp=[[-1]*2 for i in range(42)]
dp[0][0]=0
bit=[0]*41
for i in range(41):
    mask=1<<(40-i)
    cnt0,cnt1=0,0
    for j in range(N):
        if A[j]&mask:
            cnt1+=1
        else:
            cnt0+=1
    cost0,cost1=cnt1*mask,cnt0*mask
    if dp[i][1]!=-1:
        dp[i+1][1]=max(dp[i+1][1],dp[i][1]+max(cost0,cost1))
    if K&mask:
        dp[i+1][1]=max(dp[i+1][1],dp[i][0]+cost0)
        dp[i+1][0]=max(dp[i+1][0],dp[i][0]+cost1)
    else:
        dp[i+1][0]=dp[i][0]+cost0
print(max(dp[-1]))