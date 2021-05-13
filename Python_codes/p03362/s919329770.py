#サンプルが罠ってパターンもあるんだぜ


def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError("n is int-type.")
    if n < 2:
        raise ValueError("n is more than 2")
    data = [i for i in range(2, n + 1)]
    for d in data:
        data = [x for x in data if (x == d or x % d != 0)]
    return data

N = int(input())
primes = get_sieve_of_eratosthenes(5000)
ans=[]

inde=0
while len(ans)<N:
    if primes[inde]%5 == 1:
        ans.append(primes[inde])
    inde+=1

print(" ".join(list(map(str,ans))))
