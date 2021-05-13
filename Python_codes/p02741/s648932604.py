a = [1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14,
     1, 5, 1, 5, 2, 2, 1, 15, 2, 2, 5, 4, 1, 4, 1, 51]

num = input()
num = int(num) - 1

if 0 <= num <= 31:
    print(a[num])
else:
    pass
