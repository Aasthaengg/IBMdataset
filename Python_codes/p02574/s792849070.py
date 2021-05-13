from sys import exit
from math import gcd

def eratosthenes(n):
    '''
    n以下の整数の素数判定/列挙 (n > 1)
    O(NloglogN)
    '''
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    judge = [i for i in range(n+1)]
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
                judge[j] = i

    return judge


n = int(input())
a = list(map(int, input().split()))

l = eratosthenes(10**6+1)

flag = True
used = [False] * (10**6+1)
for v in a:
    while v > 1:
        d = l[v]

        if used[d]:
            flag = False
        else:
            used[d] = True
        
        while v % d == 0:
            v //= d

if flag:
    print('pairwise coprime')
    exit()

g = a[0]
for v in a:
    g = gcd(g, v)

print('setwise coprime' if g == 1 else 'not coprime')