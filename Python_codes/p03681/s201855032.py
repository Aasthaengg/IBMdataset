import math

N, M = map(int, input().split())
mod = 10 ** 9 + 7

if abs(N - M) > 1:
    print(0)
elif abs(N - M) == 1:
    f = math.factorial(min(N, M))
    res = f % mod
    res *= f * max(N, M) % mod
    print(res % mod)
else:
    f = math.factorial(N)
    res = 2 * f % mod
    res *= f
    print(res % mod)
