L = input()
dp1 = 2
dp2 = 1
MOD = 10**9+7
for c in L[1:]:
  if c=='1':
    ndp1 = 2*dp1
    ndp2 = dp1 + 3*dp2
  else:
    ndp1 = dp1
    ndp2 = 3*dp2
  dp1,dp2 = ndp1%MOD,ndp2%MOD
print((dp1+dp2)%MOD)