def main():
    n, m, d = list(map(int, input().split(' ')))
    if d > 0:
        print(2 * (n - d) * (m - 1) / (n ** 2))
    else:
        print((m - 1) / n)


if __name__ == '__main__':
    main()