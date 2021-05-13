import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    t,x = list(map(int, sys.stdin.readline().split()))
    print(t/x)


if __name__ == '__main__':
    main()
