n = int(input())
a = 64
while True:
    if a <= n:
        print(a)
        exit()
    elif n == 1:
        print(1)
        exit()
    a = a // 2