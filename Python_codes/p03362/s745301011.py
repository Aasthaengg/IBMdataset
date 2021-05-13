import itertools

n = int(input())

def Eratosthenes(n):
    Primes = [2]
    All = [x for x in range(3, n+1)]
    check = True
    max_check = int((n**(1/2)//1))
    while check:
        if All[0] > max_check:
            return Primes + All[1:]
        All = [x for x in All if x % Primes[-1] != 0]
        Primes.append(All[0])


Primes = Eratosthenes(55555)

Primes_select = [x for x in Primes if x % 5 == 1]
Ans = Primes_select[:n]
ans = [str(x) for x in Ans]
print(' '.join(ans))