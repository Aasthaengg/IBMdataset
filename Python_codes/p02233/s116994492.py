n = int(input())
dp = [0]*(n+1)
def fibo(n):
  if n <2:
    return 1
  if dp[n]  > 0:
    return dp[n]
  dp[n] = fibo(n-1) + fibo(n -2)
  return dp[n]
print(fibo(n))
