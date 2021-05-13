def comb(n, k):
    ret = 1
    for i in range(1, k + 1):
        ret = ret * (n - i + 1) % MOD        
        ret = ret * pow(i, MOD - 2, MOD) % MOD

    return ret


X, Y = map(int, input().split())

MOD = 10 ** 9 + 7

if (2 * Y - X < 0 or 2 * X - Y < 0
        or (2 * Y - X) % 3 != 0
        or (2 * X - Y) % 3 != 0):
    print(0)
    exit()

a = (2 * Y - X) // 3
b = (2 * X - Y) // 3

print(comb(a + b, a))
