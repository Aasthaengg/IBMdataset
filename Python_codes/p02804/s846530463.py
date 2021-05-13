n,k = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
if k == 1:
  print(0)
  quit()
mod = 10**9+7
fact = [1]
fact_inv = [0]*(n+4)
for i in range(n+3):
  fact.append(fact[-1]*(i+1)%mod)
fact_inv[-1] = pow(fact[-1],mod-2,mod)
for i in range(n+2,-1,-1):
  fact_inv[i] = fact_inv[i+1]*(i+1)%mod
def mod_comb_k(n,k,mod):
  if n*k == 0:
    return 1
  return fact[n] * fact_inv[k] % mod * fact_inv[n-k] %mod

maxS = 0
minS = 0
for i in range(0,n):
  if n-i-1 >= k-1:
    minS += (mod_comb_k(n-i-1,k-1,mod)*a[i])%mod
  if i >= k-1:
    maxS += (mod_comb_k(i,k-1,mod)*a[i])%mod
  minS %= mod
  maxS %= mod
print((maxS-minS)%mod)