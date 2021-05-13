def main():
    x, y = map(int, input().split())
    if y > x:
        x, y = y, x
    while y > 0:
        r = x % y
        x = y
        y = r

    print(x)


if __name__ == '__main__':
    main()
