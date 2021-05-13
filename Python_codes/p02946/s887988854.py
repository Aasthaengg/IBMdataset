def main():
    k, x = map(int, input().split())

    left = max(x - k + 1, -1000000)
    right = min(x + k - 1, 1000000)

    for i in range(left, right + 1):
        print(i, end=" ")


if __name__ == "__main__":
    main()
