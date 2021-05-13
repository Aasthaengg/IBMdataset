n = int(input())
a = list(map(int,input().split()))
dp = [0]*(n)
dp[0] = 1000

for i in range(1,n):
    tmp = dp[i-1]
    for j in range(i):
        k = dp[j]//a[j]
        m = dp[j]-a[j]*k
        tmp = max(tmp,m + a[i] * k)
    dp[i] = tmp

print(dp[n-1])