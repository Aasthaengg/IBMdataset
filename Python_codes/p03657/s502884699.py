import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B = list(map(int, sys.stdin.buffer.readline().split()))
    print('Possible' if A%3 == 0 or B%3 == 0 or (A+B)%3 == 0 else 'Impossible')


if __name__ == '__main__':
    main()
