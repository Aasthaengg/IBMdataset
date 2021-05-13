A, B = map(int, input().split())

def prime_factorize(n):
    res = set()
    i = 2
    while i * i <= n:
        if n % i == 0:
            res.add(i)
            while n % i == 0:
                n //= i
        i += 1
    if n != 1:
        res.add(n)
    return res

ans = prime_factorize(A) & prime_factorize(B)
print(len(ans) + 1)