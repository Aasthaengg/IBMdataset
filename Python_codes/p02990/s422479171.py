MOD = 10**9 + 7
N, K = map(int, input().split())

def combination(n, k, MOD):
  #nCk % MOD を出力する関数(0<=k<=nは暗に仮定)
  frac = [1]*(n+1)
  for i in range(1, n+1):
    frac[i] = (frac[i-1]*i)%MOD
  return (frac[n]*pow(frac[k], MOD-2, MOD)*pow(frac[n-k], MOD-2, MOD))%MOD

for i in range(1, K+1):
  if(N-K-i+1<0):
    print(0)
  else:
    print((combination(K-1, i-1, MOD)*combination(N-K+1, i, MOD))%MOD)