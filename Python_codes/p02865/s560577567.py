def main(n: int):
    if n % 2 == 0:
        print(int((n / 2) - 1))
    else:
        print(int((n - 1) / 2))


if __name__ == "__main__":
    n = int(input())

    main(n)
