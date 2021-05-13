def main():
    a, b, c = map(int, input().split())

    ans = b + min(a + b + 1, c)

    print(ans)


if __name__ == "__main__":
    main()
