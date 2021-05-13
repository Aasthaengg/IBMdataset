def main():
    n, m = map(int, input().split())
    f = 2 ** m
    g = n + 18 * m
    t = 100 * g * f
    print(t)


if __name__ == '__main__':
    main()
