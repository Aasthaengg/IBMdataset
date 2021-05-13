n, m = map(int, input().split())
c = [int(i) for i in input().split()]
dp = [5*10**4]*(n+1)

dp[0] = 0
for i in range(1,n+1):
  dp[i] = min([dp[i-j]+1 for j in c if i>=j])
print(dp[n])  
