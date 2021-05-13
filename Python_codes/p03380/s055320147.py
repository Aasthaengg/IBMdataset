import sys
from bisect import bisect_left

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    MAX = max(A)
    A = A[:-1]
    target = MAX / 2
    idx = bisect_left(A, target)

    if idx == 0:
        print(MAX, A[0])
    elif idx == N - 1:
        print(MAX, A[-1])
    else:
        if abs(target - A[idx]) < abs(target - A[idx - 1]):
            print(MAX, A[idx])
        else:
            print(MAX, A[idx - 1])


if __name__ == "__main__":
    main()
