import math
N, M = map(int, input().split())
mod = 10**9+7

if abs(N-M) > 1:
  print(0)
  exit()

if N < M:
  N, M = M, N

if N == M:
  ans = math.factorial(N)
  ans %= mod
  ans *= math.factorial(M)
  ans %= mod
  ans *= 2
  ans %= mod
else:
  ans = math.factorial(M)
  ans %= mod
  ans *= math.factorial(N)
  ans %= mod
  

print(ans)