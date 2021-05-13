def perm(n,r,p):
  if (r < 0) or (n < r):
    return 0
  return fac[n]*finv[n-r]%p

n = pow(10,5)*2+10
MOD = pow(10,9)+7

fac = [-1]*(n+1); fac[0] = 1; fac[1] = 1 #階乗
finv = [-1]*(n+1); finv[0] = 1; finv[1] = 1 #階乗の逆元
inv = [-1]*(n+1); inv[0] = 0; inv[1] = 1 #逆元
for i in range(2,n+1):
  fac[i] = fac[i-1]*i%MOD
  inv[i] = MOD - inv[MOD%i]*(MOD//i)%MOD
  finv[i] = finv[i-1]*inv[i]%MOD


N,M = map(int,input().split())
if abs(N-M) > 1:
  print(0);exit()
if N == M:
  ans = fac[N]*perm(M,N-1,MOD)*2
else:
  if M > N:
    N,M = M,N
  ans = fac[N]*perm(M,N-1,MOD)
print(ans%MOD)