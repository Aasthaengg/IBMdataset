for i in range(0, 10001):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if x > y:
        temp = int(x)
        x = y
        y = temp
    print(f'{x} {y}')
