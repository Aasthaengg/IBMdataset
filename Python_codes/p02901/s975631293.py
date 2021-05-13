n,m=map(int,input().split())

dp=[float('inf')]*(2**n)
dp[0]=0

for i in range(m):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    cnt=0
    for j in c:
        cnt+=2**(j-1)
    
    for j in range(2**n):
        dp[j|cnt]=min(dp[j|cnt],dp[j]+a)


if dp[2**n-1]>10**10:
    print(-1)

else:
    print(dp[2**n-1])