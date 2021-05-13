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

q, *LR = map(int, open(0).read().split())
P = set(sieve(10**5))
d = {-1:0}
s = 0
for i in range(1, 10**5, 2):
    s += i in P and (i+1)//2 in P
    d[i] = s
for l, r in zip(LR[::2], LR[1::2]):
    print(d[r] - d[l-2])