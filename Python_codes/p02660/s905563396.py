#!/usr/bin/env python3
# 整数の入力
n = int(input())

#素因数分解
def PrimeFactorization(n):
    ret = []
    for i in range(2, int(n ** 0.5)+1):
        if n % i != 0:
            continue
        
        exp = 0
        while n % i == 0:
            exp += 1
            ret.append(i**exp)
            n //= i

    if n != 1:
        ret.append(n)

    ret.sort()
    return ret

a = PrimeFactorization(n)
ans = 0
for i in a:
    if n % i == 0:
        ans += 1
        n //= i

print(ans)