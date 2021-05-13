if __name__ == '__main__':
   n, m = map(int,input().split())
   a = set([int(input()) for i in range(m)])
   broken = [False] * (n+1)
   for i in range(n+1):
      if i in a:
         broken[i] = True

   MOD = 1000000007


   dp = [0 for i in range(n+1)]
   dp[0] = 1
   if 1 in a:
      dp[1] = 0
   else:
      dp[1] = 1

   for i in range(2,n+1):
      if broken[i-1] and broken[i-2]:
         dp[i] = 0
      elif broken[i-1]:
         dp[i] = dp[i-2] % MOD
      elif broken[i-2]:
         dp[i] = dp[i-1] % MOD
      else:
         dp[i] = (dp[i-1] + dp[i-2]) % MOD

   print(dp[n])
