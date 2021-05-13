n=int(input())
l=list(map(int,input().split()))
dp=[10**55 for i in range(n)]
dp[0]=0
dp[1]=abs(l[1]-l[0])
for i in range(2,n):
    dp[i] = min(dp[i], dp[i-1] + abs(l[i] - l[i - 1]))
    dp[i] = min(dp[i], dp[i-2] + abs(l[i] - l[i - 2]))
print(dp[n-1])

