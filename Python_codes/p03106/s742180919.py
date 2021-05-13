def main():
    a, b, k = map(int, input().split())

    m = min(a, b)
    c = 1

    for i in reversed(range(1, m + 1)):
        if a % i == 0 and b % i == 0:
            if c == k:
                print(i)
                exit()
            else:
                c += 1


if __name__ == '__main__':
    main()
