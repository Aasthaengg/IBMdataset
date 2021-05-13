def main():
    n = int(input())

    c = 0
    for i in range(n + 1)[1:]:
        if (1 <= i and i <= 9) or (100 <= i and i <= 999) or (10000 <= i and i <= 99999):
            c += 1

    print(c)


if __name__ == '__main__':
    main()
