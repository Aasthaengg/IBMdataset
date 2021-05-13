def main():
    k, a, b = list(map(int, input().split()))
    if b - a <= 2:
        print(k + 1)
    else:
        c = max(0, (k - (a - 1)) // 2)
        print((b - a) * c + k - 2 * c + 1)


if __name__ == '__main__':
    main()
