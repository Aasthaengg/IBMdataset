n = int(input())
a = list(map(int,input().split()))
dp = [0]*n
dp[0] = 1000
for i in range(1,n):
  dp[i] = dp[i-1]
  for j in range(i):
    kabu = dp[j]//a[j]
    money = dp[j]+(a[i]-a[j])*kabu
    dp[i] = max(dp[i],money)
print(dp[-1])