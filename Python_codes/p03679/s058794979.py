import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    X, A, B = list(map(int, sys.stdin.buffer.readline().decode().split()))
    if B - A > X:
        print('dangerous')
    elif A >= B:
        print('delicious')
    else:
        print('safe')


if __name__ == '__main__':
    main()
