x = int(input())

if 6 < x < 11:
    print(2)
    exit()
elif 1 <= x <= 6:
    print(1)
    exit()

if x % 11 == 0:
    print((x // 11) * 2)
else:
    num = (x // 11) * 2
    amari = x % 11
    if 0 <= amari <= 6:
        print(num + 1)
    else:
        print(num + 2)
