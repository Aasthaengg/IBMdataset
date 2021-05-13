import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    for a, b in zip(A, B):
        if a < b:
            cnt += (b - a) // 2
        else:
            cnt -= a - b

    if cnt < 0:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
