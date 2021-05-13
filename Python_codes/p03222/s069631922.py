h,w,k=map(int,input().split())
mod=10**9+7
fib=[1,1]
for i in range(6):
  fib.append(fib[-2]+fib[-1])
dp=[[0]*w for i in range(h+1)]
dp[0][0]=1
for i in range(h):
  for j in range(w):
    if w==1:
      dp[i+1][j]=dp[i][j]
    elif j==0:
      dp[i+1][j]=(dp[i][j]*fib[j]*fib[w-j-1]+dp[i][j+1]*fib[j]*fib[w-j-2])%(mod)
    elif j==w-1:
      dp[i+1][j]=(dp[i][j-1]*fib[j-1]*fib[w-j-1]+dp[i][j]*fib[j]*fib[w-j-1])%(mod)
    else:
      dp[i+1][j]=(dp[i][j-1]*fib[j-1]*fib[w-j-1]+dp[i][j]*fib[j]*fib[w-j-1]+dp[i][j+1]*fib[j]*fib[w-j-2])%(mod)
print(dp[h][k-1])