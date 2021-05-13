import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    A = defaultdict(int)

    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                tmp = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
                A[tmp] += 1

    for i in range(N):
        print(A[i + 1])


if __name__ == "__main__":
    main()
