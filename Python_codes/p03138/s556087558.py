N,K=map(int,input().split())
A=list(map(int,input().split()))

dp=[[-1]*2 for i in range(51)]
dp[50][0]=0

for i in reversed(range(50)):
    mask=1<<i
    bit1=0
    bit0=0
    for a in A:
        if a&mask:
            bit1+=1
        else:
            bit0+=1
    p1=bit0*mask
    p0=bit1*mask
    if dp[i+1][1]!=-1:
        dp[i][1]=dp[i+1][1]+max(p1,p0)
    if K&mask:
        dp[i][0]=dp[i+1][0]+p1
        dp[i][1]=max(dp[i][1],dp[i+1][0]+p0)
    else:
        dp[i][0]=dp[i+1][0]+p0
print(max(dp[0]))