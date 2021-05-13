while True:
    number = input()
    x = 0
    if number != '0':
        for i in number:
            x += int(i)
        print(x)
    else:
        break

