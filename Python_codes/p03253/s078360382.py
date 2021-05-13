import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

n, m = map(int, input().split())

MOD = 10 ** 9 + 7
factorial = [0] * (10 ** 6 + 1)
inverse = [0] * (10 ** 6 + 1)
factorial[0] = inverse[0] = 1
for i in range(1, 10 ** 6 + 1):
    factorial[i] = (factorial[i-1] * i) % MOD
    inverse[i] = pow(factorial[i], MOD-2, MOD)

prime_factors = []
total = 0
i = 2
while i ** 2 <= m:
    ext = 0
    while m % i == 0:
        ext += 1
        m //= i
    if ext:
        prime_factors.append((i, ext))
        total += ext
    i += 1
if m != 1:
    prime_factors.append((m, 1))
    total += 1

ans = 1
for pf, num in prime_factors:
    ans = (ans * (factorial[num + (n-1)] * inverse[num] * inverse[n-1])) % MOD
print(ans)
