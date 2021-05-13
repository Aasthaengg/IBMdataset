def main():
    n, k = int(input()), int(input())
    x = 1

    for _ in range(n):
        x = min(2 * x, x + k)
    print(x)


if __name__ == "__main__":
    main()
