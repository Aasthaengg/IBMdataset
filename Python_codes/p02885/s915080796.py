a, b = map(int, input().split())
c = a - 2 * b
if c < 0:
    print('0')
else:
    print(c)