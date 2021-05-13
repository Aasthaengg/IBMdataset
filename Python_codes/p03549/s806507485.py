def main():
    n, m = map(int, input().split())
    t = 100 * (n + 18 * m) * 2 ** m
    print(t)


if __name__ == '__main__':
    main()
