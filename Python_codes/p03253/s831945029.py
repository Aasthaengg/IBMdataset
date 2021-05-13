from collections import defaultdict, Counter, namedtuple, deque

NN = 202020
MOD = 10**9+7
INF = float("inf")

f = [0]*NN
rf = [0]*NN
inv = [0]*NN
f[0], f[1] = 1, 1
rf[0], rf[1] = 1, 1
inv[1] = 1

for i in range(2, NN):
    f[i] = (f[i-1] * i) % MOD
    inv[i] = (-inv[MOD % i] * (MOD // i)) % MOD
    rf[i] = (rf[i-1] * inv[i]) % MOD


def C(n, r):
    return (f[n] * rf[r] * rf[n-r]) % MOD


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


n, m = map(int, input().split())
primes = Counter(prime_factorize(m))


ans = 1
for k, v in primes.items():
    ans = (ans*C(v+n-1, v))%MOD

print(ans)