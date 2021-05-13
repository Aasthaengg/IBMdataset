from math import factorial


def factorize(n):
    a = 2
    fct = []
    while a * a <= n:
        while n % a == 0:
            n //= a
            fct.append(a)
        a += 1
    if n > 1:
        fct.append(n)
    return fct


n = int(input())
f = [0] * 101
for p in factorize(factorial(n)):
    f[p] += 1
cnt24 = 0
cnt14 = 0
cnt4 = 0
ans = 0
tmp = 0
for i in range(1, n + 1):
    if f[i] >= 74:
        ans += 1
    for j in range(1, n + 1):
        if i == j:
            continue
        if f[i] >= 24 and f[j] >= 2:
            ans += 1
        if f[i] >= 14 and f[j] >= 4:
            ans += 1
        for k in range(1, n + 1):
            if i == k or j == k:
                continue
            if f[i] >= 4 and f[j] >= 4 and f[k] >= 2:
                tmp += 1
print(ans + tmp // 2)
