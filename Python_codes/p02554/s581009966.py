n = int(input())

if n == 1:
    print(0)
elif n == 2:
    print(2)
else:
    x = (10 ** 9) + 7
    a = (10 ** n) % x
    b = (9 ** n) % x
    c = (8 ** n) % x
    y = a - b * 2 + c
    if y < 0:
        y += x
    y %= x
    print(y)