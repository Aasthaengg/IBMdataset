def main():
    a, b, x = map(int, input().split())

    ans = b // x - (a - 1) // x

    print(ans)


if __name__ == "__main__":
    main()
