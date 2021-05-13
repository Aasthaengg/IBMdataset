N = int(input())
A = list(map(int, input().split()))

# 全要素の因数に2が何個あるかを数える問題

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

import collections
count = 0
for a in A:
    count += collections.Counter(prime_factorize(a))[2]
    
print(count)