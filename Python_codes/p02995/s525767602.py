def common_multiple(x, y):
    for i in range(2, min(x, y)+1):
        mod_x = x % i
        mod_y = y % i
        if (mod_x == 0 and mod_y == 0):
            return common_multiple(x // i, y // i) * i
        if (mod_x == 0):
            return common_multiple(x // i, y) * i
        if (mod_y == 0):
            return common_multiple(x, y // i) * i
    return  x * y

a = input().split(" ")
A,B,C,D=int(a[0]) - 1,int(a[1]),int(a[2]),int(a[3])

M = common_multiple(C,D)
B0 = B // C + B // D - B // M
A0 = A // C + A // D - A // M
print(B - A - B0 + A0)