N = int(input())

if N % 2 != 0:
    print(0)

else:
    fives = 0
    power = 0

    while (5 ** (power+1)) <= N:  # Nには5のpower乗まで入る
        power += 1

    for i in range(1, power+1):
        fives += N // (5 ** i) // 2

    print(int(fives))
