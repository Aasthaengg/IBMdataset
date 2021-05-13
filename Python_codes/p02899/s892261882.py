import sys
import collections
import bisect


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = [0] * n
    for i in range(n):
        B[A[i] - 1] = str(i + 1)
    print(" ".join(B))


if __name__ == '__main__':
    main()
