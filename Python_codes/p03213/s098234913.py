def prime_factorize(n):
    dic = {}
    while n % 2 == 0:
        if 2 in dic:
            dic[2] += 1
        else:
            dic[2] = 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            if f in dic:
                dic[f] += 1
            else:
                dic[f] = 1
            n //= f
        else:
            f += 2
    if n != 1:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    return dic

n = int(input())

dic = {}
for i in range(1, n+1):
    dici = prime_factorize(i)
    for key in dici:
        if key in dic:
            dic[key] += dici[key]
        else:
            dic[key] = dici[key]

num74 = 0
num24 = 0
num2 = 0
num4 = 0
num14 = 0
for key, value in dic.items():
    if value >= 74:
        num74 += 1
    if value >= 24:
        num24 += 1
    if value >= 2:
        num2 += 1
    if value >= 4:
        num4 += 1
    if value >= 14:
        num14 += 1
    
ans = num74 + num24*(num2-1) + (num4-1)*num14 + (num2-2)*(num4*(num4-1)//2)
print(ans)