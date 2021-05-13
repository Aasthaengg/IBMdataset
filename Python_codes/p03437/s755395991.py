x, y = [int(i) for i in input().split()]
if x % y == 0:
    print(-1)
else:
    i = 2
    while True:
        if i * x % y != 0:
            print(i * x)
            break
        i += 1
