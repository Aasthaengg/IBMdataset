s = int(input())

# 0 0 1e9 1 y x
# 1e9 * x - y == s
# 1e9-y == s % 1e9 (mod 1e9)
# y == (1e9 - s % 1e9) % 1e9
# -yとs の　mod 1e9が等しいので最初の指揮
# 1e9 * x = s + y
# のs + yは1e9の倍数
don = 10 ** 9

y = (don - s % don) % don
x = (s + y) // don
print('0 0 {} 1 {} {}'.format(don, y, x))
