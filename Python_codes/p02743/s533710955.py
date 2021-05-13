a, b, c = map(int, input().split())
if c - a - b <= 0:
    print('No')
else:
    if 4 * a * b < c ** 2 + a ** 2 + b ** 2 + 2 * (a * b - a * c - b * c):
        print('Yes')
    else:
        print('No')
