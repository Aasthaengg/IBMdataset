import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)


def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    m = float("inf")
    count = defaultdict(int)
    for i in range(N):
        if A[i] < m:
            m = A[i]
        else:
            count[A[i] - m] += 1
    K = list(count.keys())
    print(count[max(K)])


if __name__ == "__main__":
    main()
