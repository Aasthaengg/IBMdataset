def main():
    n = int(input())

    c = 0
    for i in range(n + 1)[1:]:
        if len(str(i)) % 2 == 1:
            c += 1

    print(c)


if __name__ == '__main__':
    main()
