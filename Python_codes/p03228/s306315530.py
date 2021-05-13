a,b,c = map(int,input().split())
x = 0
for i in range(c):
    if (int(i) + 2) % 2 == 0:
        if (a + 1) % 2 == 0:
            a = a - 1
            x = int(a / 2)
            b = b + x
            a = a - x
        else:
            x = int(a / 2)
            b = b + x
            a = a - x
    else:
        if (b + 1) % 2 == 0:
            b = b - 1
            x = int(b / 2)
            a = a + x
            b = b - x
        else:
            x = int(b / 2)
            a = a + x
            b = b - x
print(a,b)