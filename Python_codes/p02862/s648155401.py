X, Y = map(int, input().split())

MAX = 2 * 10 ** 6 + 1
MOD = 10 ** 9 + 7

# Factorial
fac = [0] * (MAX + 1)
fac[0] = 1
fac[1] = 1
for i in range(2, MAX + 1):
    fac[i] = fac[i - 1] * i % MOD
    
# Inverse factorial
finv = [0] * (MAX + 1)
finv[MAX] = pow(fac[MAX], MOD - 2, MOD)
for i in reversed(range(1, MAX + 1)):
    finv[i - 1] = finv[i] * i % MOD

def comb(n, k):
    if n < k or k < 0:
        return 0
    return (fac[n] * finv[k] * finv[n - k]) % MOD

mod = 10 ** 9 + 7
v1 = 2 * Y - X
v2 = 2 * X - Y
if (v1 >= 0 and v1 % 3 == 0 and v2 >= 0 and v2 % 3 == 0):
    a = v1 // 3
    b = v2 // 3
    print(comb(a + b, a))
else:
    print(0)
