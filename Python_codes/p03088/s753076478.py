import numpy as np
N = int(input())
MOD = 10**9+7
dp = np.zeros(64,np.int64)
pdp = np.ones(64,np.int64)
a = 16
b = 4
pdp[0*a+2*b+1] = 0
pdp[0*a+1*b+2] = 0
pdp[2*a+0*b+1] = 0
dic = {}
dic[0] = 'A'
dic[1] = 'C'
dic[2] = 'G'
dic[3] = 'T'
for i in range(N-3):
  for j in range(64):
    x = j//16
    y = (j-x*16)//4
    z = j%4
    m = 16*y+4*z
    if y==2 and z==0:
      for h in range(4):
        if h==1:
          continue
        dp[m+h] += pdp[j]
    elif y==0 and z==2:
      for h in range(4):
        if h==1:
          continue
        dp[m+h] += pdp[j]
    elif y==0 and z==1:
      for h in range(4):
        if h==2:
          continue
        dp[m+h] += pdp[j]
    elif x==0 and y==2:
      for h in range(4):
        if h==1:
          continue
        dp[m+h] += pdp[j]
    elif x==0 and z==2:
      for h in range(4):
        if h==1:
          continue
        dp[m+h] += pdp[j]
    else:
      for h in range(4):
        dp[m+h] += pdp[j]
  dp %= MOD
  pdp = np.copy(dp)
  dp = np.zeros(64,np.int64)
print(pdp.sum()%MOD)