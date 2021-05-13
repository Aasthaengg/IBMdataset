N = int(input())

power = 1

while power <= N:
    power *= 2
    if power == N:
        print(power)
        exit()
    elif power > N:
        print(power // 2)
        exit()
