def main2():
    x = int(input())
    r, m = divmod(x, 100)
    x -= r * 100

    count = 0

    while(x > 0):
        if x >= 5:
            x -= 5
            count += 1
        elif x >= 4:
            x -= 4
            count += 1
        elif x >= 3:
            x -= 3
            count += 1
        elif x >= 2:
            x -= 2
            count += 1
        elif x >= 1:
            x -= 1
            count += 1

    if r >= count:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main2()