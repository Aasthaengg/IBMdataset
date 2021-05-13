def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = True
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i] is False:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return is_prime


n = int(input())
ans = []
is_prime = sieve_of_eratosthenes(55555)

for i in range(2, 55556):
    if is_prime[i] is True and i % 10 == 1:
        ans.append(i)
        if len(ans) == n:
            break

print(*ans)
