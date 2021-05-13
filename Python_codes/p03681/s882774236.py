import math

N, M = map(int, input().split())
mod = 10**9+7

if abs(N - M) >= 2:
    print(0)
elif N == M:
    print(((math.factorial(N) % mod) * (math.factorial(M) % mod) * 2) % mod)
else:
    print(((math.factorial(N) % mod) * (math.factorial(M) % mod)) % mod)