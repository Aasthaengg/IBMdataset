def main():
    a, b, c = map(int, input().split())
    d, e, f = abs(a - b), abs(b - c), abs(c - a)

    print(min(d + e, e + f, f + d))


if __name__ == "__main__":
    main()
