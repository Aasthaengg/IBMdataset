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
    N, K = read_values()
    res = 0
    P = K // 2 if K % 2 == 0 else K
    for a in range(P, N + 1, P):
        k = a // K + 1
        l = (N + a) // K
        res += (l - k + 1) ** 2

    print(res)


if __name__ == "__main__":
    main()