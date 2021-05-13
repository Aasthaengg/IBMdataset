n,m = map(int,input().split())
ais = []
for _ in range(m):
    ai = int(input())
    ais.append(ai)
dp = [0]*(n+1)
dp[0]=1
if len(ais)>0 and ais[0]==1:
  dp[1]=0
  ais.pop(0)
else:
  dp[1]=1
for i in range(2,n+1):
    if len(ais)>0 and ais[0]==i:
        dp[i] = 0
        ais.pop(0)
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%1000000007)
