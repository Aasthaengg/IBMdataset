n = int(input())

if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    print((1 + n - 1) * (n - 1) // 2)