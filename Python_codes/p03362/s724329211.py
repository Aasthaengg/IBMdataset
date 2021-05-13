n = int(input())

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    ret = [2]
    limit = int(n**0.5)
    data = [i for i in range(3, n+1, 2)]
    while True:
        p = data[0]
        if p >= limit:
            break
        else:
            ret.append(p)
            data = [e for e in data if e % p != 0]
    return ret + data

sieve = get_sieve_of_eratosthenes(55555)
ANS = []

for prime in sieve:
    if prime % 5 == 1:
        ANS.append(prime)

print(*ANS[:n])