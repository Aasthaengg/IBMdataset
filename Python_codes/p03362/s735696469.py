n = int(input())

def get_sieve_of_atkin(n):  # O(n)
    is_prime = {i: False for i in range(5, n + 1)}
    limit = int(n**0.5) + 1
    for x in range(1, limit):
        for y in range(1, limit):
            k = 4 * x**2 + y**2
            if k <= n and (k % 12 == 1 or k % 12 == 5):
                is_prime[k] = not is_prime[k]
            k = 3 * x**2 + y**2
            if k <= n and k % 12 == 7:
                is_prime[k] = not is_prime[k]
            k = 3 * x**2 - y**2
            if x > y and k <= n and k % 12 == 11:
                is_prime[k] = not is_prime[k]
    for k in range(5, limit):
        if is_prime[k]:
            i = 1
            while i * k**2 <= n:
                is_prime[i * k**2] = False
                i += 1
    return [2, 3] + [i for i in range(5, n + 1, 2) if is_prime[i]]

sieve = get_sieve_of_atkin(55555)
ANS = []

for prime in sieve:
    if prime % 5 == 1:
        ANS.append(prime)

print(*ANS[:n])