h,w,k = (int(x) for x in input().split())
MOD = 1000000007

dp=[[0]*(w+2) for _ in range(h+2)]
fib = [0]*(w+1)

# 初期条件
fib[1] = 1
dp[0][1] = 1
# フィボナッチ
for i in range(2,w+1):
  fib[i] = fib[i-1] + fib[i-2]
  
for i in range(1, h+1):
  for j in range(1, w+1):
    dp[i][j] = (dp[i - 1][j - 1]*fib[j - 1]*fib[w - j + 1]+dp[i - 1][j]*fib[j]*fib[w - j + 1]+dp[i - 1][j + 1]*fib[j]*fib[w - j])%MOD
                                                                                                                          
print(dp[h][k])    
