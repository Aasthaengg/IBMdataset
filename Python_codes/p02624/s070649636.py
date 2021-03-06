# エラトステネスの篩
def make_prime_table(N):
    sieve = list(range(N + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(2, int(N ** 0.5) + 1):
        if sieve[i] != i:
            continue
        for j in range(i * i, N + 1, i):
            if sieve[j] == j:
                sieve[j] = i
    return sieve


def f(X):
    t = []
    a = X
    while a != 1:
        if len(t) != 0 and t[-1][0] == prime_table[a]:
            t[-1][1] += 1
        else:
            t.append([prime_table[a], 1])
        a //= prime_table[a]
    result = 1
    for _, n in t:
        result *= n + 1
    return result


N = int(input())

prime_table = make_prime_table(N)
result = 0
for K in range(1, N + 1):
    result += K * f(K)
print(result)
