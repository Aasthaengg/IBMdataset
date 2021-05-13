def main():
    A, P = map(int, input().split())

    pieces = 3 * A + P
    ans = pieces // 2

    print(ans)


if __name__ == "__main__":
    main()
