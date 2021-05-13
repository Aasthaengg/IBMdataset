def main():
    x = int(input())

    n = x // 100

    if 0 <= x - 100 * n <= 5 * n:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
