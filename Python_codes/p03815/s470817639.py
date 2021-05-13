X = int(input())

a, b = divmod(X, 11)

if b == 0:
    print(a * 2)
elif b <= 6:
    print(a * 2 + 1)
else:
    print(a * 2 + 2)
