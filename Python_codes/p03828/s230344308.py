import math

N = int(input())

dic = {}
for n in range(2, N + 1):
    p = 2
    while 1 < n and p <= math.sqrt(n):
        if n % p == 0:
            while n % p == 0:
                n //= p
                dic[p] = dic.get(p, 0) + 1
        p += 1

    if n > 1:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1

ret = 1
for v in dic.values():
    ret *= v + 1

print(ret % (10 ** 9 + 7))