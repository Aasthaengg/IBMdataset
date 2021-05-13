n = int(input())
arr = list(map(float,input().split()))

dp=[]
for i in range(n+1):
    dp.append([0]*(n+1))
dp[1][0]=(1-arr[0])
dp[1][1]=arr[0]

for i in range(2,n+1):
    for j in range(0,i+1):
        dp[i][j]= dp[i-1][j-1]*arr[i-1] + dp[i-1][j]*(1-arr[i-1])
ans=0
for i in range(n//2+1,n+1):
    ans+=dp[n][i]

print(ans)


