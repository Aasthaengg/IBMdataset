def resolve():
    a, b = map(int, input().split())
    print(a + b if a + b < 10 else "error")


if __name__ == "__main__":
    resolve()
