import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, A = [int(sys.stdin.buffer.readline().rstrip()) for _ in range(2)]
    print('Yes' if N%500 <= A else 'No')


if __name__ == '__main__':
    main()
