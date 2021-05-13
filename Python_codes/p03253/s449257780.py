from collections import Counter
N,M = map(int,input().split())
primes = []
d = 2
while d**2<=M:
    if M % d == 0:
        M //= d
        primes.append(d)
    else:
        d += 1

if M != 1:
    primes.append(M)

cnt = Counter(primes)

def choose(n,k):
    import math
    return math.factorial(n)//(math.factorial(n-k)*math.factorial(k))
ans = 1
for v in cnt.values():
    ans *= choose(v+(N-1),v)
mod = 10**9 +7
ans %= mod
print(ans)
