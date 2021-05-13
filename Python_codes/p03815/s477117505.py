x = int(input())

y = x // 11
z = x % 11

if x <= 6:
    print(1)
elif z == 0:
    print(y * 2)
elif z <= 6:
    print(y * 2 + 1)
else:
    print(y * 2 + 2)