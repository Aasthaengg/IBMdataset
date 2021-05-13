# D - Five, Five Everywhere

def sieve_of_eratosthenes(n):
    primes = []
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return primes

n = int(input())
A = sieve_of_eratosthenes(55555)

ans = []
for a in A:
    if a%5 == 1:
        ans.append(a)
        if len(ans) == n:
            break

print(' '.join(map(str, ans)))