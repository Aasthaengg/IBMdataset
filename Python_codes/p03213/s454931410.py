N = int(input())

sieve = [0] * 101
sieve[0] = -1
sieve[1] = -1
for i in range(2, 101):
    if sieve[i] != 0:
        continue
    sieve[i] = i
    for j in range(i * i, 101, i):
        if sieve[j] == 0:
            sieve[j] = i

d = {}
for i in range(2, N + 1):
    while i != 1:
        d.setdefault(sieve[i], 0)
        d[sieve[i]] += 1
        i //= sieve[i]


result = 0
# 75 = 5 * 5 * 3
# x ^ 4 * y ^ 4 * z ^ 2 の約数の個数は75個
n2 = 0
n4 = 0
for k in d:
    if 2 <= d[k] <= 3:
        n2 += 1
    elif d[k] >= 4:
        n4 += 1
result += n2 * n4 * (n4 - 1) // 2 + n4 * (n4 - 1) * (n4 - 2) // 2
# x ^ 14 * y ^ 4 の約数の個数は75個
n4 = 0
n14 = 0
for k in d:
    if 4 <= d[k] <= 13:
        n4 += 1
    elif d[k] >= 14:
        n14 += 1
result += n4 * n14 + n14 * (n14 - 1)
# x ^ 24 * y ^ 2 の約数の個数は75個
n2 = 0
n24 = 0
for k in d:
    if 2 <= d[k] <= 23:
        n2 += 1
    elif d[k] >= 24:
        n24 += 1
result += n2 * n24 + n24 * (n24 - 1)
# x ^ 74 の約数の個数は75個
n74 = 0
for k in d:
    if d[k] >= 74:
        n74 += 1
result += n74
print(result)
