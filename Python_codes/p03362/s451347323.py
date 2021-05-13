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
N = int(input())
prime = primes(55555)
ans = [0]*N
for i in range(N):
    for k in prime:
        if k % 5 == 1 and k not in ans:
            ans[i] = k
            break
print(*ans)
