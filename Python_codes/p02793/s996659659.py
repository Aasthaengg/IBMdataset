from collections import defaultdict
import sys

input = sys.stdin.buffer.readline
mod = 10 ** 9 + 7


def modinv(a, mod):
    return pow(a, mod - 2, mod)


# 素因数分解
def prime_factor(n):
    # (素因数, 数)のリストで出てくる
    d = defaultdict(int)
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            d[i] += 1
            n //= i
    if n != 1:
        d[n] += 1
    return list(d.items())


n = int(input())
if n == 1:
    print(1)
    exit()
A = list(map(int, input().split()))
LCM = defaultdict(int)
for i in range(n):
    temp = prime_factor(A[i])
    for key, value in temp:
        t = LCM[key]
        LCM[key] = max(t, value)
lcm = 1
for key, val in LCM.items():
    lcm *= pow(key, val)
ans = 0
for i in range(n):
    gyaku = modinv(A[i], mod)
    ans += lcm * gyaku
    ans %= mod
print(ans)
