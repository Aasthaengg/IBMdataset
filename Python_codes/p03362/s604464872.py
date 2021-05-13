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
p = the_sieve_of_eratosthenes(55555)
ans = []
i = 0
for _ in range(n):
    while True:
        if p[i] % 10 == 1:
            ans.append(p[i])
            i += 1
            break
        i += 1
print(" ".join(map(str, ans)))