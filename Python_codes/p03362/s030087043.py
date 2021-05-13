def eratosthenes(n):
    is_prime = [True for i in range(n+1)]
    is_prime[0], is_prime[1] = False, False
    prime = []
    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
            for j in range(2*i, n+1, i):
                is_prime[j] = False
    return prime


N = int(input())

prime = eratosthenes(55555)
ans = []
for p in prime:
    if p % 5 == 1:
        ans.append(p)
    if len(ans) == N:
        break
    
print(*ans)
