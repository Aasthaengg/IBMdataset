n=int(input())
l=[1,6,36,6**3,6**4,6**5,6**6,9,9**2,9**3,9**4,9**5]
l.sort(reverse=True)
dp=[float("inf")]*1000000
dp[0]=0
for i in range(1,n+1):
    for j in l:
        if i-j>=0:
            dp[i]=min(dp[i],dp[i-j]+1)
print(dp[n])