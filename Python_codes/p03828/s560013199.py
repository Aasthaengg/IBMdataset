def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def count(N, p):
    cnt = 0
    while N != 0:
        cnt += N // p
        N //= p
    return cnt

N = int(input())
mod = 10 ** 9 + 7
Primes = primes(N)
ans = 1
for p in Primes:
    ans *= (count(N, p) + 1)
    ans %= mod
print(ans)