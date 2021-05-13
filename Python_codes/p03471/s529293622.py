N, Y = map(int, input().split())

max_10000 = Y // 10000
for x in range(max_10000 + 1):
    if x > N:
        continue

    rem = Y - 10000 * x

    max_5000 = rem // 5000
    for y in range(max_5000 + 1):
        if x + y > N:
            continue

        rem_2 = rem - 5000 * y
        if x + y + rem_2 // 1000 == N:
            print('{} {} {}'.format(x, y, rem_2 // 1000))
            exit()


print('{} {} {}'.format(-1, -1, -1))
