import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    a, b = list(map(str, sys.stdin.buffer.readline().decode().split()))
    print('H' if a == 'H' and b == 'H' or a == 'D' and b == 'D' else 'D')


if __name__ == '__main__':
    main()
