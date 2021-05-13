def the_sieve_of_eratosthenes(i):
    s = [j for j in range(2, i + 1)]
    j = 0
    while True:
        if j >= i - 3:
            for k in range(len(s) - 1, 0, -1):
                if s[k] == 0:
                    del s[k]
            return s
        if s[j] != 0:
            for k in range(2 * s[j] - 2, i - 1, s[j]):
                s[k] = 0
        j += 1

n = int(input())
p = the_sieve_of_eratosthenes(n)
c = [1] * len(p)
for i in range(2, n + 1):
    if not i in p:
        j = 0
        while True:
            if i == 1 or j == len(p):
                break
            if i % p[j] == 0:
                i /= p[j]
                c[j] += 1
            else:
                j += 1
a1, a2, a3, a4, a5 = 0, 0, 0, 0, 0
ans = 0
for i in c:
    if i >= 2:
        a1 += 1
    if i >= 4:
        a2 += 1
    if i >= 14:
        a3 += 1
    if i >= 24:
        a4 += 1
    if i >= 74:
        a5 += 1
ans = ((a1 - 2) * a2 * (a2 - 1) // 2) + (a2 - 1) * a3 + (a1 - 1) * a4 + a5
print(ans)