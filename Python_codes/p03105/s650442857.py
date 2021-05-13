def main():
    a, b, c = map(int, input().split())

    d = b // a

    print(min(c, d))


if __name__ == "__main__":
    main()
