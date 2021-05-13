n,k = list(map(int,input().split()))
arr = list(map(int,input().split()))
dp=[999999999]*n
dp[0]=0
for i in range(len(arr)):
    for j in range(i,i+k+1):
        if j<n:
            dp[j]=min(dp[j],dp[i] + abs(arr[j] - arr[i]))
    #print(dp)
print(dp[n-1])