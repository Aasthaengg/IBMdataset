import sys

mod=10**9+7
fib=[1]*10
for i in range(2,10):
  fib[i]=fib[i-1]+fib[i-2]
#print(fib)

H,W,K=map(int,input().split())
if W==1:
  print(1)
  sys.exit()

dp=[[0]*(W+1) for _ in range(H+1)]
dp[0][1]=1

for i in range(1,H+1):
  dp[i][1]=(fib[W-1]*dp[i-1][1]+fib[W-2]*dp[i-1][2])%mod
  dp[i][W]=(fib[W-2]*dp[i-1][W-1]+fib[W-1]*dp[i-1][W])%mod
  for j in range(2,W):
    dp[i][j]=(fib[j-2]*fib[W-j]*dp[i-1][j-1]+fib[j-1]*fib[W-j]*dp[i-1][j]+fib[j-1]*fib[W-j-1]*dp[i-1][j+1])%mod
    
#print(dp)
print(dp[H][K])