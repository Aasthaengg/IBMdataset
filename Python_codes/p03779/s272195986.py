def main():
    X = int(input())
    n = 1
    while True:
        if (n - 1) * n // 2 < X <= n * (n + 1) // 2:
            break
        n += 1
    print(n)


if __name__ == '__main__':
    main()