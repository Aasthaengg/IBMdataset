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
from scipy.misc import comb
from collections import Counter
n, m = map(int, input().split())
c = Counter(prime_factorize(m))
l = [i[1] for i in c.most_common()]
ans = 1
for i in l:
    ans *= comb(i + n - 1, i, exact=True)
    ans %= 10 ** 9 + 7
print(int(ans))