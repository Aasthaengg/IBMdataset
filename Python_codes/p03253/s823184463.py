import math
def prime_factorize(n):
    ListPrime = []
    while n % 2 == 0:
        ListPrime.append(2)
        n //= 2
    f = 3
    while f*f <= n:
        if n % f == 0:
            ListPrime.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        ListPrime.append(n)
    return ListPrime

N,M = map(int,input().split())
A = list(set(prime_factorize(M)))
List = []
for i in range(len(A)):
    List.append(prime_factorize(M).count(A[i]))
Listans = 1
for i in range(len(List)):
    Listans *= (math.factorial(List[i]+N-1)//(math.factorial(List[i])*math.factorial(N-1)))
print(Listans%(10**9+7))
