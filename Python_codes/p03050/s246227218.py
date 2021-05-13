import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def main():
    N = int(input())
    res = 0
    for r in range(int(N ** 0.5), 0, -1):
        if N % r == 0:
            m = N // r - 1
            if r >= m:
                continue
            res += m
    print(res)


if __name__ == "__main__":
    main()