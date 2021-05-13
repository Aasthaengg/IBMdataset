def main():
    A, B, C = map(int, input().split())

    ans = C - (A - B)

    print(max(ans, 0))


if __name__ == "__main__":
    main()
