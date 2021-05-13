mod = 10**9+7
# nCr
def calcComb(n,r):
  mul, div = 1, 1
  for i in range(r):
    mul *= (n-i)
    div *= (i+1)
    mul %= mod
    div %= mod

  return mul * pow(div,mod-2,mod) % mod

n,m = map(int, input().split())

i = 2
ans = 1
while i*i <= m:
  if m%i == 0:
    cnt = 0
    while m!=1 and m%i == 0:
      cnt += 1
      m //= i
    ans *= calcComb(n+cnt-1, n-1)
    ans %= mod
  i += 1

if m != 1:
  ans *= calcComb(n+1-1, n-1)
  ans %= mod

print(ans)
