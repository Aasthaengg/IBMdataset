# vim: fileencoding=utf-8


def main():
    n, a, b = map(int, input().split())
    if (b - a) % 2 == 0:
        print("Alice")
    else:
        print("Borys")


if __name__ == "__main__":
    main()
