N, K = map(int, input().split())

def ncr(n, r, p):
  num = den = 1
  for i in range(r):
    num = (num * (n - i)) % p
    den = (den * (i + 1)) % p
  return (num * pow(den, p - 2, p)) % p
p=10**9+7

for i in range(1, K+1):
  ans = (ncr(N-K+1, i, p) % p) * (ncr(K-1, i-1, p) % p) % p
  print(ans)