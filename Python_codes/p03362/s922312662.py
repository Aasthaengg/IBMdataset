primes = []

for n in range(6, 55556, 5):
    k = 2
    while k * k <= n:
        if not n % k:
            break
        k += 1
    else:
        primes.append(n)

print(*primes[:int(input())])
