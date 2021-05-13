L = int(input())
S = str(L)
N = len(str(L))
MOD = 10**9+7
dp0 = [0]*N
dp1 = [0]*N
dp0[0] = 1
dp1[0] = 2
for i in range(1,N):
  if S[i]=='1':
    dp0[i] = dp0[i-1]*3+dp1[i-1]
    dp1[i] = dp1[i-1]*2
  else:
    dp0[i] = dp0[i-1]*3
    dp1[i] = dp1[i-1]
  dp0[i] %= MOD
  dp1[i] %= MOD
print((dp0[-1]+dp1[-1])%MOD)
