
def sieve(n):
    prime = []

    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, n + 1):
        if is_prime[i]:
            prime.append(i)

            for j in range(2 * i, n + 1, i):
                is_prime[j] = False

    return prime, is_prime


N = int(input())
prime, _ = sieve(10 ** 5 + 10)
for v in prime:
    if v >= N:
        print(v)
        break
