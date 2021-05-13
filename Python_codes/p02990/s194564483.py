N, K = map(int, input().split())
L = N - K
mod = 10 ** 9 + 7
m = mod - 2
def POW(a, b):
  bin_b = []
  while b:
    bin_b.append(b % 2)
    b >>= 1
  ret = 1
  for j in reversed(bin_b):
    ret = (ret * ret) % mod
    if j == 1:
      ret = (ret * a) % mod
  return ret
comb1 = 1
comb2 = 1
for i in range(1, K+1):
  P = POW(i, mod-2)
  comb1 = (comb1 * (L + 2 - i)) % mod
  comb1 = (comb1 * P) % mod
  print((comb1 * comb2) % mod)
  comb2 = (comb2 * (K - i)) % mod
  comb2 = (comb2 * P) % mod