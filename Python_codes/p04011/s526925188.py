def main():
    n, k, x, y = int(input()), int(input()), int(input()), int(input())

    if n <= k:
        print(n * x)
    else:
        print(k * x + (n - k) * y)


if __name__ == "__main__":
    main()
