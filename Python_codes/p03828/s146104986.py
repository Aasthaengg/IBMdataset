from collections import defaultdict
from collections import Counter

# nを素因数分解
# 各素因数を数え上げる場合はcounterを使うとよい
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

N = int(input())
    
d = defaultdict(lambda: 0)

if N == 1:
    print(1)
else:
    for i in range(2, N+1):
        a = prime_factorize(i)
        c = Counter(a)
        for k, v in c.items():
            d[k] += v

    count = 1
    for v in d.values():
        count *= (v + 1)
        count %= int(1e9+7)
    print(count)