n = int(input())

primes = [2]
for x in range(3, 55556):
    chk = True
    for tmp in primes:
        if tmp ** 2 > x:
            break
        if x % tmp == 0:
            chk = False
    if chk:
        primes.append(x)

p2 = []
for prime in primes:
    if prime % 5 == 1:
        p2.append(prime)

p3 = p2[:n]

print(' '.join([str(pp) for pp in p3]))
