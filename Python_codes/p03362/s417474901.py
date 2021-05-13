n = int(input())

import math

def sieve(n):
    ass = []
    is_prime = [True]*(n+1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(math.sqrt(n))+1):
        if not is_prime[i]:
            continue
        for j in range(i*2, n+1, i):
            is_prime[j] = False
    for i in range(n+1):
        if is_prime[i]:
            ass.append(i)
    return(ass)

S = sieve(55555)
T = []
for i in range(len(S)):
    if S[i]%5 == 1:
        T.append(S[i])
print(*T[0:n])
