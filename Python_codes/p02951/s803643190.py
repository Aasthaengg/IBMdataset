a, b, c = map(int, input().split())
dif = a - b
if c >= dif:
    print(c - dif)
else:
    print('0')