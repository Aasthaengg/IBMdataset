from collections import defaultdict as dd
N = int(input())

def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct
res = 1
MOD = 10**9+7
dic = dd(int)
for i in range(1,N+1):
    f = factorize(i)
    for val in f:
        dic[val] += 1
for val in dic.values():
    res = res*(val+1)%MOD
print(res)
