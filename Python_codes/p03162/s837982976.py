ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n = ni()
dp = [[0]*3 for _ in range(n)]

a,b,c = nm()

dp[0][0]=a
dp[0][1]=b
dp[0][2]=c

for i in range(1,n):
  a,b,c = nm()
  dp[i][0] = max(dp[i-1][1]+a, dp[i-1][2]+a)
  dp[i][1] = max(dp[i-1][0]+b, dp[i-1][2]+b)
  dp[i][2] = max(dp[i-1][0]+c, dp[i-1][1]+c)

print(max([dp[n-1][0],dp[n-1][1],dp[n-1][2]]))
