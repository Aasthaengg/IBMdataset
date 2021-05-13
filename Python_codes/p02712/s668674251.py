def main():
    N = int(input())

    s = 0
    for x in range(1, N + 1):
        if x % 3 == 0:
            continue
        if x % 5 == 0:
            continue
        s += x
    print(s)


if __name__ == '__main__':
    main()
