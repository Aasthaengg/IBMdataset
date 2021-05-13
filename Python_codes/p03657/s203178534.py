def resolve():
    a, b = map(int, input().split())
    print("Possible") if any([True for i in [a, b, a + b] if i % 3 == 0]) else print("Impossible")


if __name__ == "__main__":
    resolve()
