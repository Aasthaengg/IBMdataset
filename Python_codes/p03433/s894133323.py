# vim: fileencoding=utf-8


def main():
    N = int(input())
    A = int(input())
    x = N % 500
    if A >= x:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
