n=int(input())
h=[1,6,6**2,6**3,6**4,6**5,6**6,9,9**2,9**3,9**4,9**5,9**6]
dp=[10**9]*(n+1)

dp[0]=0
for i in range(n):
    for j in range(len(h)):
        if i+h[j]<=n:
            dp[i+h[j]]=min(dp[i+h[j]],dp[i]+1)
    
print(dp[n])