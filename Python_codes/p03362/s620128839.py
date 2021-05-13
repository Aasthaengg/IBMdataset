N = int(input())

def get_primes(n):
    '''
    素数テーブルの作成
    '''
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i, b in enumerate(is_prime):
        if b:
            yield i

primes_and_mod1 = []
for i in get_primes(55999):
    if i % 5 == 1:
        primes_and_mod1.append(i)

print(*primes_and_mod1[:N], sep=" ")

