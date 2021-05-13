N,T=map(int,input().split())
A,B=[],[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a);B.append(b)
dp=[[0,0] for i in range(T)]

for i in range(N):
    for j in reversed(range(T)):
        dp[j][1]=max(dp[j][1],dp[j][0]+B[i])
        if j-A[i]>=0:
            dp[j][0]=max(dp[j-A[i]][0]+B[i],dp[j][0])
            dp[j][1]=max(dp[j-A[i]][1]+B[i],dp[j][1])
ans=max(dp[T-1][0],dp[T-1][1])
print(ans)