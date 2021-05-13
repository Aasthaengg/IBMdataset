n = int(input())

for i in range(3, n+1):
    if i % 3 == 0:
        print('', i, end='')
        continue

    x = i

    while x >= 1:
        if x % 10 == 3:
            print('', i, end='')
            break

        x = int(x/10)

print()