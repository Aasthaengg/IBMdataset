def resolve():
    a, b, c = map(int, input().split())
    if a + b < c - 1:
        print(2 * (a + b) + 1 - a)
    else:
        print(b + c)


if __name__ == "__main__":
    resolve()
