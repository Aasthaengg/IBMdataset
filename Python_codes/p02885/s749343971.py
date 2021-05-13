def main():
    A, B = map(int, input().split())

    if A - 2 * B > 0:
        ans = A - 2 * B
    else:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
