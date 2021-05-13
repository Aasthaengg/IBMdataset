x = int(input())


def prime_factorize(n):
    r = []
    while n % 2 == 0:
        r.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            r.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        r.append(n)
    return r


for i in range(x, x+100):
    l = prime_factorize(i)
    if i in l:
        l.remove(i)
    if not l:
        print(i)
        exit()