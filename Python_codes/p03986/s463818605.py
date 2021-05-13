def main():
    x = input()

    s = 0
    count = 0
    for cur in x:
        if cur == "S":
            s += 1
        else:
            if s != 0:
                s -= 1
            else:
                count += 2

    print(count)


if __name__ == '__main__':
    main()