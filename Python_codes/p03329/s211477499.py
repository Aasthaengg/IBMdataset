dp=[1000000 for i in range(100010)]
dp[0]=0
for n in range(1,100010):
  power=1
  while(power<=n):
    dp[n]=min(dp[n],dp[n-power]+1)
    power*=6
  power=1
  while(power<=n):
    dp[n]=min(dp[n],dp[n-power]+1)
    power*=9

i=int(input())
print(dp[i])