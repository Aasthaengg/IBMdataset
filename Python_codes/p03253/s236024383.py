import math
from collections import Counter
n, m = map(int, input().split())

prime_count = Counter()
for i in range(2, math.ceil(math.sqrt(m))+1):
    while m % i == 0:
        m /= i
        prime_count[i] += 1
if m > 1:
    prime_count[int(m)] += 1

def ncr(n, r, p):
    num = den = 1
    for i in range(r):
        num = (num * (n - i)) % p
        den = (den * (i + 1)) % p
    return (num * pow(den, p - 2, p)) % p
p=10**9+7 

ans = 1
for k, v in prime_count.items():
    ans *= ncr(v+n-1, v, p)
    ans %= p

print(ans)
