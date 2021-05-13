import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    a, b = map(str, sys.stdin.readline().split())

    if a == "H" and b == "H":
        ret = "H"
    elif a == "H" and b == "D":
        ret = "D"
    elif a == "D" and b == "H":
        ret = "D"
    elif a == "D" and b == "D":
        ret = "H"

    print(ret)


if __name__ == '__main__':
    main()
