def factorization(n):
    res = []
    m = 2
    while m ** 2 <= n:
        if n % m == 0:
            cnt = 0
            while n % m == 0:
                cnt += 1
                n //= m
            res.append([m, cnt])
        m += 1

    if n > 1:
        res.append([n, 1])

    return res


n = int(input())

mod = 10 ** 9 + 7

cnt = [0] * (n+1)
for i in range(2, n+1):
    for j, k in factorization(i):
        cnt[j] += k

res = 1
for c in cnt:
    if c > 0:
        res = res * (c + 1) % mod

print(res)