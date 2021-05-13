mod = 10**9 + 7

N_MAX = 10**5+1
fact = [1] * N_MAX
for i in range(1,N_MAX):
  fact[i] = (fact[i-1]*i) % mod
  
def nCr(n,r):  
  if n < r:
    return 0
  return (fact[n] * pow(fact[r]*fact[n-r] ,mod-2,mod))% mod

n,k = map(int,input().split())
A = sorted(list(map(int,input().split())))

mi = 0
ma = 0

for i in range(1,n):
  m = nCr(n-i,k-1)
  mi += A[i-1] * m
  ma += A[-i]  * m
  
print((ma - mi)%mod)