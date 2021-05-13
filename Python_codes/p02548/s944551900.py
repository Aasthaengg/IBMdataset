import collections

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



nu=int(input())
total=0
for p in range(1,nu):
    s=collections.Counter(prime_factorize(p))
    sama=1
    for j in s.values():
        sama=sama*(j+1)
    total+=sama
print(total)