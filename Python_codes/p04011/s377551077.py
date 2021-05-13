def main():
    n = int(input())
    k = int(input())
    x = int(input())
    y = int(input())

    if n - k >= 0:
        print(x * k + y * (n - k))
    else:
        print(x * n)


if __name__ == "__main__":
    main()