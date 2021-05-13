import sys
import os

MOD = 10 ** 9 + 7


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = int(sys.stdin.buffer.readline().rstrip())
    print('Hello World') if N == 1 else print(sum(int(sys.stdin.buffer.readline().rstrip()) for _ in range(2)))

if __name__ == '__main__':
    main()
