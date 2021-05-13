S = int(input())
dp=[1]+[0 for i in range(S)]
i = 3
k=1000000007
if S <3:
  print(0)
else:
  while i <= S:
    dp[i]=(dp[i-1]+dp[i-3])%k
    i+=1
  print(dp[S])