import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    B = deque([])
    for i, a in enumerate(A):
        if i % 2 == 0:
            B.append(a)
        else:
            B.appendleft(a)

    if N % 2 != 0:
        B = reversed(B)

    print(*B)

    return


if __name__ == '__main__':
    main()
