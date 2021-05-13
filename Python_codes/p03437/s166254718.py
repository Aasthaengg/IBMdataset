def main():
    x, y = map(int, input().split())
    if x % y != 0:
        print(x)
    else:
        print(-1)


if __name__ == '__main__':
    main()

