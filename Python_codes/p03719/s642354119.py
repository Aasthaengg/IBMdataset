import sys
import os

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    A, B, C = il()
    print('Yes' if A <= C <= B else 'No')


if __name__ == '__main__':
    main()
