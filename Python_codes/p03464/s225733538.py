import sys
import math


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    K = int(input())
    A = list(map(int, input().split()))
    min_ch = 2
    max_ch = 3
    if A[-1] != 2:
        print(-1)
        return
    for i in range(K):
        n = K - i - 1
        if max_ch < A[n]:
            print(-1)
            return
        a = math.ceil(min_ch / A[n])
        b = math.floor(max_ch / A[n])
        min_ch = A[n] * a
        if min_ch > max_ch:
            print(-1)
            return
        max_ch = A[n] * (b + 1) - 1
    print(min_ch, max_ch)


if __name__ == "__main__":
    main()
