import math
import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    op = sum(B) - sum(A)
    p = 0
    for i in range(N):
        if B[i] > A[i]:
            p += math.ceil((B[i] - A[i]) / 2)

    if p > op:
        print("No")
    else:

        print("Yes")


if __name__ == "__main__":
    main()
