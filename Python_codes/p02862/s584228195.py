MOD = 10**9 + 7

def fac(n):
    ans = 1
    for i in range(1, n + 1):
        ans = ans * i % MOD
    return ans

X, Y = map(int, input().split())

a, b = (2 * Y - X) // 3, (2 * X - Y) // 3
if (2 * X - Y) % 3 != 0 or a*b < 0:
    print(0)
else:
    print((fac(a + b) * pow(fac(a), MOD-2, MOD) * pow(fac(b), MOD-2, MOD)) % (10**9 + 7))