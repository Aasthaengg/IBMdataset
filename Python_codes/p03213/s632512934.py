# エラトステネスの篩
def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i):
            if sieve[j] == j:
                sieve[j] = i
    return sieve


def prime_factorize(n):
    result = []
    while n != 1:
        p = prime_table[n]
        c = 0
        while n % p == 0:
            n //= p
            c += 1
        result.append((p, c))
    return result


N = int(input())

prime_table = make_prime_table(N)
d = {}
for i in range(2, N + 1):
    for p, c in prime_factorize(i):
        d.setdefault(p, 0)
        d[p] += c

# 75 = 5 * 5 * 3
#    = 15 * 5
#    = 25 * 3
#    = 75
n74 = 0
n24 = 0
n14 = 0
n4 = 0
n2 = 0
for k in d:
    if d[k] >= 74:
        n74 += 1
    if d[k] >= 24:
        n24 += 1
    if d[k] >= 14:
        n14 += 1
    if d[k] >= 4:
        n4 += 1
    if d[k] >= 2:
        n2 += 1

result = 0
# x ^ 4 * y ^ 4 * z ^ 2 の約数の個数は75個
result += n4 * (n4 - 1) // 2 * (n2 - 2)
# x ^ 14 * y ^ 4 の約数の個数は75個
result += n14 * (n4 - 1)
# x ^ 24 * y ^ 2 の約数の個数は75個
result += n24 * (n2 - 1)
# x ^ 74 の約数の個数は75個
result += n74
print(result)
