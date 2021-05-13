X, Y = map(int,input().split())

MOD = 10**9 + 7

def comb(n, r):
    if n < r or n < 0 or r < 0:
        return 0

    n += 1
    over = 1
    under = 1
    for i in range(1,r + 1):
      over = over * (n - i) % MOD
      under = under * i % MOD
    return over * pow(under, MOD - 2, MOD) % MOD

if (X + Y) % 3 != 0:
    print(0)
else:
    a = (2 * X - Y) // 3
    b = (2 * Y - X) // 3
    print(comb(a+b, a))

