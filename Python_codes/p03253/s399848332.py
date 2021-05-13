import collections
import math

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

def nCr(n,r):
  #print(n,r)
  return (FAC[n]*INV[n-r]*INV[r])%MOD

n,m = map(int,input().split())

MOD = 10**9 + 7
FAC = [1]
INV = [1]
N = int(math.log(m,2))+n+1
for i in range(1,N+1):
  FAC.append((FAC[i-1]*i) % MOD)
  INV.append(pow(FAC[-1],MOD-2,MOD))

c = collections.Counter(prime_factorize(m))
#print(c)
ans = 1
for k,v in c.items():
  #print(k,v)
  ans *= nCr(v+n-1,v)
  ans %= MOD
print(ans)