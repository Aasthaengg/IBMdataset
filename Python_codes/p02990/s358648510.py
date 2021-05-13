import math
def comb(n, r):
  if n - r < 0:
    return 0
  else:
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
MOD = 10**9 + 7
N, K = map(int, input().split(' '))
red = N - K
for i in range(K):
  res = comb(red + 1, i + 1) * comb(K - 1, i)
  res %= MOD
  print(res)