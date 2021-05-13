def main(n: int, a: int, b: int):
    if a > b:
        print(0)
        return

    if n == 1:
        if a == b:
            print(1)
        else:
            print(0)
        return

    if n == 2:
        if a > b:
            print(0)
        else:
            print(1)
        return

    print((n - 2) * (b - a) + 1)


if __name__ == "__main__":
    n, a, b = map(int, input().split())

    main(n, a, b)
