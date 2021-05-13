import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    N, M = read_values()
    A = read_list()
    R = {}
    R[0] = 1
    S = 0
    for a in A:
        S += a
        S %= M
        R[S] = R.setdefault(S, 0) + 1

    res = 0
    for r in R.values():
        res += r * (r - 1) // 2

    print(res)


if __name__ == "__main__":
    main()
