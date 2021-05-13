def main():
    h = int(input())

    if h == 1:
        minimum = 1
    else:
        if h % 2 == 1:
            h -= 1

        minimum = 0
        power = 0
        while True:
            minimum += 2 ** power
            power += 1

            if 2 ** power > h:
                break

    print(minimum)


if __name__ == '__main__':
    main()