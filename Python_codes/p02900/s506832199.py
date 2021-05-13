def prime_factorize(n):
    # 素因数分解して素数と1の集合を作る
    a = {1}
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return a


A, B = map(int, input().split())
cds = prime_factorize(A) & prime_factorize(B)
print(len(cds))