import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    S = input()
    check = [
        "AKIHABARA",
        "KIHABARA",
        "AKIHBARA",
        "AKIHABRA",
        "AKIHABAR",
        "KIHBARA",
        "KIHABRA",
        "KIHABAR",
        "AKIHBRA",
        "AKIHBAR",
        "AKIHABR",
        "KIHBRA",
        "KIHABR",
        "KIHBAR",
        "AKIHBR",
        "KIHBR",
    ]
    if S in check:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
