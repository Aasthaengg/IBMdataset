mod = 10 ** 9 + 7


def mod_mul(a, b):
    return a * b % mod


N, M = map(int, input().split())
*x, = map(int, input().split())
*y, = map(int, input().split())

sx = sum(mod_mul(_x, i - (N - 1 - i)) for i, _x in enumerate(x))  # _x * i - _x * (N - 1 - i)
sy = sum(mod_mul(_y, i - (M - 1 - i)) for i, _y in enumerate(y))  # _y * i - _y * (M - 1 - i)
print(sx * sy % mod)
