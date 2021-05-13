a, b, c = map(int, input().split())

# n*a /b >
if (a % 2 == 0 and b % 2 == 0 and c % 2 != 0):
    print('NO')
elif (a % 2 == 0 and b % 2 != 0 and c % 2 == 0):
    print('NO')


else:
    count = 0
    while count < 10 ** 7:
        count += 1
        if ((a * count) % b == c):
            print('YES')
            exit()

    print('NO')
