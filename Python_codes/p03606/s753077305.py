import sys
import os


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = int(sys.stdin.readline().rstrip())
    ret = 0
    for n in range(N):
        l, r = list(map(int, sys.stdin.readline().split()))
        ret += r - l + 1

    print(ret)


if __name__ == '__main__':
    main()
