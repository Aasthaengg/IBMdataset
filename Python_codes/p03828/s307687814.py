import math

def factorize(n):
    d = {}
    temp = int(math.sqrt(n))+1
    for i in range(2, temp):
        while n%i== 0:
            n //= i
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    if d == {}:
        d[n] = 1
    else:
        if n in d:
            d[n] += 1
        elif n != 1:
            d[n] =1
    return d

n = int(input())

if n == 1:
    print(1)
    exit()

mod = 10**9+7
D = {}
for i in range(2, n+1):
    d = factorize(i)
    for k, v in d.items():
        if k not in D:
            D[k] = v
        else:
            D[k] += v
ans = 1
for v in D.values():
    ans *= (v+1)
    ans %= mod
print(ans)