N = int(input())
mod = 1000000007

primes = list()

for i in range(2, N+1):
    for j in primes:
        if i % j == 0:
            break
    else:
        primes.append(i)

ans = 1
for p in primes:
    x = 1
    q = p
    while q <= N:
        for i in range(2, N+1):
            if i % q == 0:
                x += 1
        q *= p
    ans = ans * x % mod

print(ans)
