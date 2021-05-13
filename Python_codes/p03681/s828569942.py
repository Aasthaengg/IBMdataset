from functools import reduce

def fac(n, p):
    return reduce(lambda x, y: x * y % p, range(1, n + 1))

N, M = [int(x) for x in input().split()]
p = 10 ** 9 + 7
if abs(N - M) >= 2:
    ans = 0
elif N == M:
    ans = 2 * fac(N, p) * fac(M, p) % p
else:
    ans = fac(N, p) * fac(M, p) % p

print(ans)