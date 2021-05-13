x, y = map(int, input().split())

if (x + y) % 3 or (x > y * 2) or (x * 2 < y):
  print(0)
else:
  MOD = 10 ** 9 + 7
  MAX = 10 ** 6

  fac = [1] * MAX
  inv = [1] * MAX
  finv = [1] * MAX
  for i in range(2, MAX):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = (- inv[MOD % i] * (MOD // i)) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD

  def com(n, k):
    if n < 0 or k < 0:
      return 0
    if n < k:
      return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

  a = (x + y) // 3
  b = (a - abs(x - y)) // 2
  print(com(a, b))