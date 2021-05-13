def sieve(n):
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    for i in range(2, n+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime


MAX_A = 55555
is_prime = sieve(MAX_A)
N = int(input())
a = []
for i in range(MAX_A+1):
    if is_prime[i] and i % 5 == 1:
        a.append(str(i))
        if len(a) == N:
            break
print(' '.join(a))
