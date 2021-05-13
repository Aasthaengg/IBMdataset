n=int(input())
a=list(map(int,input().split()))
dp=[1000]*(n+1) #dp[i]:=i日目の取引が終わった時の最大値
for i in range(n):
    for j in range(i):
        dp[i]=max(dp[i],a[i] * (dp[j]//a[j]) + dp[j]%a[j])
    dp[i]=max(dp[i],dp[i-1])
print(dp[n-1])