a, b = map(int, input().split())

ab = a + b

x = ab // 2

xmod = ab % 2

if (xmod == 0):
    print(x)

else:
    print(x + 1)