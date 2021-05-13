from math import sqrt
def sieve(n):
    if n <= 4:
        return list(range(2, n))
    def _sieve_of_eratosthenes(n):
        limit = int(sqrt(n))+1
        table = [1] * n
        table[0] = table[1] = 0
        for i in range(2, limit):
            if table[i]:
                for j in range(i**2, n, i):
                    table[j] = 0
        return [i for i in range(2, n) if table[i]]
    return _sieve_of_eratosthenes(n)
print(*[x for x in sieve(5555) if x % 5 == 1][:int(input())])