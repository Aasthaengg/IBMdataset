def factorial(n, mod=10**9+7):
    a = 1
    for i in range(1,n+1):
        a = a * i % mod
    return a

N, M = map(int, input().split())
MOD = 10**9 + 7
if N < M:
  N, M = M, N

if N > M + 1:
  ans = 0
elif N == M + 1:
  ans = (factorial(N) * factorial(M)) % MOD
else:
  ans = (2 * factorial(N) ** 2) % MOD

print(ans)