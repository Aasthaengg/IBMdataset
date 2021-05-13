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
    min_factor = [-1] * (n+1)
    min_factor[0] = 0
    min_factor[1] = 1
    
    for i in range(2, n+1):
        if is_prime[i]:
            min_factor[i] = i
            for j in range(i*2, n+1, i):
                is_prime[j] = False
                if min_factor[j] == -1:
                    min_factor[j] = i

    return min_factor


n = int(input())
a = list(map(int, input().split()))

l = eratosthenes(10**6+1)

flag = True
used = [False] * (10**6+1)
for v in a:
    s = set()
    while v > 1:
        if l[v] not in s:
            if used[l[v]]:
                flag = False
                break
            else:
                s.add(l[v])
                used[l[v]] = True
        
        v //= l[v]

if flag:
    print('pairwise coprime')
    exit()

g = 0
for v in a:
    g = gcd(g, v)

print('setwise coprime' if g == 1 else 'not coprime')