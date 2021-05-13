import numpy as np
MOD = 10**9+7
n = int(input())
dp = np.zeros((n+1, 4, 4, 4), dtype=np.int64)
dp[0, 3, 3, 3] = 1
for i in range(n):
  for a in range(4):
    for b in range(4):
      for c in range(4):
        for d in range(4):
          if d==1:
            if (a==0 and b==2) or (a==0 and c==2) or (b==0 and c==2) or (c==0 and b==2):
              continue
          if b==0 and d==2 and c==1:
            continue
          dp[i+1, b, c, d] += dp[i, a, b, c]
          dp[i+1, b, c, d] %= MOD
print(dp[n].sum()%MOD)