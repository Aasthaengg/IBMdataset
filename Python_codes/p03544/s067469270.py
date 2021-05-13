n = int(input())

dp = [-1] * 100
dp[0] = 2
dp[1] = 1

def f(x):
  if x == 0:
    return dp[0]
  
  if x == 1:
    return dp[1]

  if dp[x] == -1:
    dp[x] = f(x-1) + f(x-2)
    return dp[x]
  else:
    return dp[x]

print(f(n))
