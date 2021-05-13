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

from collections import Counter
N = int(input())
c = Counter([])
ans = 1
for i in range(1,N+1):
    c = c + Counter(prime_factorize(i))
for x in c.values():
    ans = (ans*(x+1)) % 1000000007
print(ans)