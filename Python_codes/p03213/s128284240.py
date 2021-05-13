from collections import Counter

n = int(input())

def prime_factorize(n):
    i = 2
    temp = n
    result = []
    while(i * i <= n):
        count = 0
        while temp % i == 0:
            count += 1
            temp //= i
        if count > 0:
            result.append([i, count])
        i += 1
    if temp != 1:
        result.append([temp, 1])
    return result

c = Counter()
for i in range(1, n + 1):
    pf = prime_factorize(i)
    for p in pf:
        c[p[0]] += p[1]

count2 = 0
count4 = 0
count15 = 0
count25 = 0
count75 = 0
for i, v in c.items():
    if v >= 74:
        count75 += 1
    if v >= 24:
        count25 += 1
    if v >= 14:
        count15 += 1
    if v >= 4:
        count4 += 1
    if v >= 2:
        count2 += 1


b = count4 * (count4 - 1) * (count2 - 2) // 2
c = count15 * (count4 - 1)
d = count25 * (count2 - 1)
e = count75


print(b + c + d + e)
