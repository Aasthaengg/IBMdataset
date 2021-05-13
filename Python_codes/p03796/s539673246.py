
n = int(input())


def func(times):
    power = 1
    divide_num = 10 ** 9 + 7

    for i in range(times):
        power *= (i + 1)
        power %= divide_num

    print(power)


func(times=n)
