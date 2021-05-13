n, a, b = map(int, input().split())

if b < a:
    print(0)
elif n == 1:
    if a == b:
        print(1)
    else:
        print(0)
else:
    small = a * (n - 2)
    big = b * (n - 2)
    num = big - small + 1
    print(num)