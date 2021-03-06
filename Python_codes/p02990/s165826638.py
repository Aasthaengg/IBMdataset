# フェルマーの小定理
N, K = map(int, input().split())

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


n = max(K, N - K + 1)
fac = make_factorial_table(n)

result = []
for i in range(1, K + 1):
    result.append(mcomb(K - 1, i - 1) * mcomb(N - K + 1, i) % m)
#print('\n'.join(str(i) for i in result))
print(*result, sep='\n')
