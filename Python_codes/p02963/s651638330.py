A = int(input())

a = 10**9 - A % (10**9)
b = A // (10**9) + 1


if b > 10**9:
    print(0, 0, 10**9, 0, 0, 10**9)
else:
    print(0, 0, 10**9, 1, a, b)