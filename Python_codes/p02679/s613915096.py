import math, collections
N = int(input())
AB = [[int(_) for _ in input().split()] for _ in range(N)]
mod = 10**9 + 7
C = collections.Counter()
gcd = math.gcd
a0 = 0
for a, b in AB:
    if a == b == 0:
        a0 += 1
    elif a == 0:
        C[0, -1] += 1
    else:
        g = gcd(a, b)
        a //= g
        b //= g
        if a < 0:
            a *= -1
            b *= -1
        C[a, b] += 1
ans = 1
for a, b in C:
    if C[b, -a]:
        continue
    elif C[-b, a]:
        ans *= (pow(2, C[a, b], mod) + pow(2, C[-b, a], mod) - 1) % mod
        ans %= mod
    else:
        ans *= pow(2, C[a, b], mod)
        ans %= mod
ans += a0 - 1
ans %= mod
print(ans)
