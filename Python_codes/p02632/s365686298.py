K = int(input())
S = input()

m = 1000000007


def make_factorial_table(n):
    result = [0] * (n + 1)
    result[0] = 1
    for i in range(1, n + 1):
        result[i] = result[i - 1] * i % m
    return result


def mcomb(n, k):
    if n == 0 and k == 0:
        return 1
    if n < k or k < 0:
        return 0
    return fac[n] * pow(fac[n - k], m - 2, m) * pow(fac[k], m - 2, m) % m


fac = make_factorial_table(len(S) - 1 + K)

result = 0
for i in range(K + 1):
    t = pow(26, i, m) * mcomb(len(S) - 1 + K - i, len(S) - 1)
    t %= m
    t *= pow(25, K - i, m)
    t %= m
    result += t
    result %= m
print(result)
