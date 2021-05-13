def resolve():
    X = int(input())
    if X <= 99:
        print('0')
        return

    for i in range(1, 1000 + 1):
        if 100 * i + 6 + (i - 1) * 5 <= X <= 100 * i + 99:
            print('0')
            return
    print('1')

    return

resolve()