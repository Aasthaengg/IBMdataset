import collections

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
  
U = 2*10**6
MOD = 10**9+7
 
fact = [1]*(U+1)
fact_inv = [1]*(U+1)
 
for i in range(1,U+1):
  fact[i] = (fact[i-1]*i)%MOD
fact_inv[U] = pow(fact[U],MOD-2,MOD)
 
for i in range(U,0,-1):
  fact_inv[i-1] = (fact_inv[i]*i)%MOD
 
def comb(n,k):
  if k < 0 or k > n:
    return 0
  z = fact[n]
  z *= fact_inv[k]
  z %= MOD
  z *= fact_inv[n-k]
  z %= MOD
  return z

n, m = map(int, input().split())
c = collections.Counter(prime_factorize(m))
ans = 1
for i in c.values():
  ans *= comb(i+n-1, n-1)
  ans %= MOD
print(ans)