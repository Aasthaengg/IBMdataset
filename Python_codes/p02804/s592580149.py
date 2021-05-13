MAX = 110000
MOD = 1000000007
fac = [0]*MAX
finv = [0]*MAX
inv = [0]*MAX
fac[0] = 1
fac[1] = 1
finv[0] = 1
finv[1] = 1
inv[1] = 1
for i in range(2, MAX):
  fac[i] = fac[i-1]*i%MOD
  inv[i] = MOD - inv[MOD%i]*(MOD//i)%MOD
  finv[i] = finv[i-1]*inv[i]%MOD
def COM(n, k):
  if n < 0 or k < 0 or n < k:
    return 0
  return fac[n]*(finv[k]*finv[n-k]%MOD)%MOD

N, K = map(int, input().split())
As = list(map(int, input().split()))
As.sort()
r = 0
for i in reversed(range(N)):
  r = (r+As[i]*COM(i, K-1))%1000000007
  r = (r-As[i]*COM(N-i-1, K-1))%1000000007
  #print(r)
print(r)
