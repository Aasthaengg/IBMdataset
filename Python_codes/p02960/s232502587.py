S = input()
dp = 13*[0]
dp[0] = 1
mod = 10**9+7

for s in S:
  if s=="?":
    dp = [sum(dp[4*(j-i)%13] for i in range(10))%mod for j in range(13)]
  else:
    dp = [dp[4*(j-int(s))%13] for j in range(13)]
    
print(dp[5])