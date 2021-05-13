# vim: fileencoding=utf-8


def main():
    x, y = map(int, input().split())
    if x * y % 2 == 0:
        print("Even")
    else:
        print("Odd")


if __name__ == "__main__":
    main()
