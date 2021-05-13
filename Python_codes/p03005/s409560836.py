def main(n: int, k: int):
    if k == 1:
        print(0)
        return

    print(n - k)


if __name__ == "__main__":
    n, k = map(int, input().split())

    main(n, k)
