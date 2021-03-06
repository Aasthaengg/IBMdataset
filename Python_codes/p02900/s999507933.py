import math

a, b = list(map(int, input().split()))

gcd = math.gcd(a, b)

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

fact = prime_factorize(gcd)
print(len(set(fact)) + 1)
