from math import ceil, sqrt

def prime_factorize_tuple(n):
    ret = []
    tmp = n
    for i in range(2, ceil(sqrt(n))):
        if tmp % i == 0:
            count = 0
            while tmp % i == 0:
                count += 1
                tmp //= i
            ret.append((i, count))

    if tmp != 1:
        ret.append((tmp, 1))

    if not ret:
        ret.append([n, 1])  # n = 1

    return ret

n = int(input())
ans = 0
for i in range(1, n + 1, 2):
    tmp = 1
    for prime, count in prime_factorize_tuple(i):
        tmp *= (count + 1)
    if tmp == 8:
        ans += 1
print(ans)
