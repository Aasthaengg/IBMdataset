from fractions import gcd

mod = 10 ** 9 + 7


def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


n = int(input())
A = list(map(int, input().split()))
lcm = A[0]
for i in range(n):
    g = gcd(lcm, A[i])
    lcm *= A[i] // g

ans = 0
for i in range(n):
    gyaku = modinv(A[i], mod)
    ans += lcm * gyaku
    ans %= mod
print(ans)
