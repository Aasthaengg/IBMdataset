import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    A.sort(reverse=True)

    i = 0
    w = h = 0
    while i < N - 1:
        if A[i] == A[i + 1]:
            if w == 0:
                w = A[i]
            else:
                h = A[i]
                break
            i += 2
        else:
            i += 1

    print(w * h)
    return


if __name__ == '__main__':
    main()
