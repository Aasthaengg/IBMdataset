N, K = map(int, input().split())
mod = 10 ** 9 + 7

def comb(n, k):
  if n < k: 
    return 0
  if n < 0 or k < 0: 
    return 0
  if k > n - k:
    return comb(n, n - k)
  mul, div = 1, 1
  for i in range(k):
    mul = mul * (n - i) % mod
    div = div * (k - i) % mod
  return mul * pow(div, mod-2, mod) % mod

for i in range(1, K + 1):
  print(comb(N - K + 1, i) * comb(K - 1, i - 1) % mod)