x = int(input())
d, mod = divmod(x, 100)
if 100 * d <= x <= 105*d:
    print(1)
else:
    print(0)
