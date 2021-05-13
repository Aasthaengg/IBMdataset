x = int(input())
a, b = divmod(x, 11)
if b > 6:
    print(a * 2 + 2)
elif b == 0:
    print(a * 2)
else:
    print(a * 2 + 1)