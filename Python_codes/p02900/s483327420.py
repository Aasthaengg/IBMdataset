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

a, b = map(int, input().split())
list_A = set(prime_factorize(a))
list_B = set(prime_factorize(b))
ans = list_A & list_B
print(len(ans) + 1)
