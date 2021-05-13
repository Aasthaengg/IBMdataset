n = int(input())
for i in range(1, n + 1):
    if (i % 3) == 0:
        print(' ' + str(i), end='')
        continue
    x = i
    while True:
        if (x == 0):
            break
        if (x % 10 == 3):
            print(' ' + str(i), end='')
            break
        x //= 10
print()