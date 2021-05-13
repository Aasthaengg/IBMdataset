def f(a, b, x):
    return (a * x) // b - a * (x // b)


def main():
    a, b, n = map(int, input().split())

    if n < b - 1:
        x = n
    else:
        x = b - 1

    print(f(a, b, x))


if __name__ == "__main__":
    main()
