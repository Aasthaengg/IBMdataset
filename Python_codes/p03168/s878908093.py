n=int(input())
A=list(float(i) for i in input().split())
dp=[[0.0 for i in range(n+1)]for j in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if i==0:
            if j>i:
                dp[i][j]=0
            else:
                dp[i][j]=1
        elif j==0:
            if i>1:
                dp[i][j]=dp[i-1][j]*(1-A[i-1])
            else:
                dp[i][j]=1-A[i-1]
        if i!=0 and j!=0:
            dp[i][j]=dp[i-1][j-1]*A[i-1]+dp[i-1][j]*(1-A[i-1])
sum=0
for s in range(n//2+1,n+1):
        sum+=dp[-1][s]
print(sum)
