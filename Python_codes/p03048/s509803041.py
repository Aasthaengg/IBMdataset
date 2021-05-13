r,g,b,n=map(int,input().split())
a=[r,g,b]

dp=[0 for _ in range(n+1)]
dp[0]=1

for i in range(3):
    for j in range(a[i],n+1):
        dp[j]+=dp[j-a[i]]

print(dp[-1])