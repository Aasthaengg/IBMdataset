def main():
    n, x, t = map(int, input().split())

    print((n//x + 1) * t if n%x != 0 else n*t // x)


if __name__ == '__main__':
    main()
