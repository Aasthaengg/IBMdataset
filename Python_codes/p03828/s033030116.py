import functools

def prime_factor(n):
    res = {}
    i = 2
    while i * i <= n:
        while n % i == 0:
            res[i] = 1
            n //= i
        i+=1
    if n != 1:
        res[n] = 1
    return res.keys()
    
N = int(input())
target = functools.reduce(lambda a, b: a * b, range(1, N + 1))

factors = prime_factor(target)
total = 1
for f in factors:
    count = 1
    while target % f == 0:
        target //= f
        count += 1
    
    total *= count

print(total % (10**9 + 7))