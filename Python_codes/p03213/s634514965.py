def prime_factor(n):
    factors = [0] * (n+1)
    for i in range(2, int(n**0.5)+1):
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count != 0:
            factors[i] = count
    if n != 1:
        factors[n] = 1
    return factors

n = int(input())
nl = [0] * (n+1)
for i in range(1, n + 1):
    l = prime_factor(i)
    for i, num in enumerate(l):
        nl[i] += num
over4 = 0
over2 = 0
over74 = 0
over14 = 0
over24 = 0
for i in nl:
    if i >= 74:
        over74 += 1
    if i >= 24:
        over24 += 1
    if i >= 14:
        over14 += 1
    if i >= 4:
        over4 += 1
    if i >= 2:
        over2 += 1
cnt = 0
cnt += over4*(over4-1)/2*(over2-2)
cnt += over24*(over2-1)
cnt += over14*(over4-1)
cnt += over74
print(int(cnt))