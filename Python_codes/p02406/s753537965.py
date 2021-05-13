n = int(input())
i = 1
while i <= n:
    x = i
    if (x % 3 == 0 or x % 10 == 3):
        print('', i, end='')
    else:
        x = int(x / 10)
        while x > 0:
            if (x % 10 == 3):
                print('', i, end='')
                break
            x = int(x / 10)
    i += 1
print()