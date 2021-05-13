import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    X, A, B = [int(sys.stdin.buffer.readline().rstrip()) for _ in range(3)]
    print((X-A)%B)


if __name__ == '__main__':
    main()
