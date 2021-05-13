i = input().split()
n, x, t = int(i[0]), int(i[1]), int(i[2])
a = n // x if divmod(n, x)[1] == 0 else n // x + 1
print(a * t)
