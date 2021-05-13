L = input()
MOD = 10**9+7
l = len(L)
dp0 = [0]*(l+1)
dp1 = [0]*(l+1)
dp1[0] = 1
for i in range(1,l+1):
  c = L[i-1]
  if c=='1':
    dp0[i] = dp0[i-1]*3+dp1[i-1]
    dp1[i] = dp1[i-1]*2
  else:
    dp0[i] = dp0[i-1]*3
    dp1[i] = dp1[i-1]
  dp0[i] %= MOD
  dp1[i] %= MOD
print((dp0[-1]+dp1[-1])%MOD)