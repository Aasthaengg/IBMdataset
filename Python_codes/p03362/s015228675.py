def sieve(n):
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if not is_prime[i]:
            continue
        else:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

n = int(input())
prime_lst = sieve(55555)

res = []
for p in prime_lst:
    if p%5==1:
        res.append(p)
print(*res[:n])