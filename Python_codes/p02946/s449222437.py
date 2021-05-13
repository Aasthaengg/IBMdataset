def main():
    k, x = map(int, input().split())

    left = x - k + 1
    right = x + k - 1

    for i in range(left, right + 1):
        print(i, end=" ")


if __name__ == "__main__":
    main()
