def main():
    a, b, c, k = map(int, input().split())

    positive = min(k, a)
    zero = min(k - positive, b)
    negative = min(k - positive - zero, c)

    max = positive - negative
    print(max)


if __name__ == '__main__':
    main()