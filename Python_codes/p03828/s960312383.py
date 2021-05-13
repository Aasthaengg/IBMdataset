MAX_PRIME = 10**5
is_prime = [1] * MAX_PRIME
primes = []
is_prime[0] = 0
is_prime[1] = 0
for i in range(MAX_PRIME):
    if is_prime[i]:
        primes.append(i)
        for j in range(2, ((MAX_PRIME-1)//i) + 1):
            is_prime[i*j] = 0

m = int(input())
mod = 10 ** 9 + 7
factor = [0] * (m+1)
for n in range(1, m+1):
    for p in primes:
        if p ** 2 > n:
            break
        while n % p == 0:
            n //= p
            factor[p] += 1
    if n > 1:
        factor[n] += 1

ans = 1
for x in factor:
    if x:
        ans *= x+1
        ans %= mod
print(ans)