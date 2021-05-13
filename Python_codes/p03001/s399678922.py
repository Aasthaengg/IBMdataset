def main():
    w, h, x, y = map(int, input().split())
    print(h * w / 2, end=" ")
    print(1 if 2 * x == w and 2 * y == h else 0)


if __name__ == '__main__':
    main()

