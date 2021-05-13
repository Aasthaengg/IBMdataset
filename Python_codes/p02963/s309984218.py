import numpy as np
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors

S = int(input())
T = S**0.5
# 平方数でない
if int(T)**2 != S:
    T = int(T)+1
    U = int(T**2 - S)
    dv = make_divisors(U)
    rootU = int(U**0.5)
    idx = 0
    a = 10**9
    for i in range(len(dv)):
        if abs(dv[i]-rootU) <= a:
            a = abs(dv[i]-rootU)
            idx = i
    a = dv[idx]
    b = int(U/a)
    res = ['0', '0', str(T), str(a), str(b), str(T)]
    print(' '.join(res))
else:
    T = int(T)
    res = ['0', '0', str(T), '0', '0', str(T)]
    print(' '.join(res))
