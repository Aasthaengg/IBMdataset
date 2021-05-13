def common_multiple(x, y):
    for i in range(2, min(x, y)+1):
        x0, y0 = x % i, y % i
        if x0 == 0 or y0 == 0:
            return common_multiple(x // i if x0 == 0 else x, y // i if y0 == 0 else y) * i
    return x * y

a = input().split(" ")
A, B, C, D = int(a[0]) - 1, int(a[1]), int(a[2]), int(a[3])

M = common_multiple(C, D)
B0 = B // C + B // D - B // M
A0 = A // C + A // D - A // M
print(B - A - B0 + A0)
