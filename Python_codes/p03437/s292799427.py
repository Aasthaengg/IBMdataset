def main(x, y):
    if x % y == 0:
        print(-1)
    else:
        print(x)


if __name__ == '__main__':
    x, y = map(int, input().split(' '))

    main(x, y)
