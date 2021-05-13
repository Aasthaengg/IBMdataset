def resolve():
    N = int(input())
    d = {}
    for i in range(2, N+1):
        for j in prime_factors(i):
            d[j] = d[j] + 1 if j in d else 1
    res = 1
    for v in d.values():
        res *= (v+1)
    print(res%(10**9+7))

def prime_factors(n):
    i = 2
    factors = []
    while i**2 <= n:
        if n % i != 0:
            i += 1
        else:
            factors.append(i)
            n = n // i
    if n > 1:
        factors.append(n)
    return factors

if '__main__' == __name__:
    resolve()

