for i in range(3000):
    string = input()
    numbers = string.split(' ')
    x, y = int(numbers[0]), int(numbers[1])
    if x == 0 and y == 0:
        break
    elif x < y:
        print(x, y)
    else:
        print(y, x)
