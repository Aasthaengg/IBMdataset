import sys
from itertools import accumulate


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(10 ** 9)


def main():
    N = int(input())
    A = sorted(list(map(int, input().split())))
    B = list(accumulate(A))
    for i in range(N - 1):
        if B[N - i - 2] * 2 >= A[N - i - 1]:
            continue
        else:
            print(i + 1)
            return
    print(N)


if __name__ == "__main__":
    main()
