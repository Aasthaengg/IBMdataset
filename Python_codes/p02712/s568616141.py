def main():
    n = int(input())

    ans = n * (n + 1) // 2 - 3 * (n // 3) * (n // 3 + 1) // 2 - 5 * \
        (n // 5) * (n // 5 + 1) // 2 + 15 * (n // 15) * (n // 15 + 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
