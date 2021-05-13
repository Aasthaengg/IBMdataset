s=int(input())

dp=[0]*(s+1)

dp[0]=1

for i in range(1,s+1):
    for j in range((i-3)+1):
        dp[i]+=dp[j]

print(dp[s]%(10**9+7))