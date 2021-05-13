from collections import defaultdict


N = int(input())
dict = defaultdict(int)


def prime_factorize(n):  # nを素因数分解してdictに保存
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    for ai in a:
        dict[ai] += 1


for i in range(1, N + 1):  # N!の素因数分解に相当する
    prime_factorize(i)

ans = 0

# p**4 * q**4 * r**2
for k1, v1 in dict.items():
    for k2, v2 in dict.items():
        for k3, v3 in dict.items():
            if k1 < k2 < k3:
                if v1 >= 2 and v2 >= 4 and v3 >= 4:
                    ans += 1
                if v1 >= 4 and v2 >= 2 and v3 >= 4:
                    ans += 1
                if v1 >= 4 and v2 >= 4 and v3 >= 2:
                    ans += 1

for k1, v1 in dict.items():
    for k2, v2 in dict.items():
        if k1 < k2:
            # p**14 * q**4
            if v1 >= 14 and v2 >= 4:
                ans += 1
            if v1 >= 4 and v2 >= 14:
                ans += 1
            # p**24 * q*2
            if v1 >= 24 and v2 >= 2:
                ans += 1
            if v1 >= 2 and v2 >= 24:
                ans += 1

# p**74
for k1, v1 in dict.items():
    if v1 >= 74:
        ans += 1

print(ans)
