import sys
from itertools import permutations

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    N = int(readline())
    print(N * (N - 1) // 2)
    return


if __name__ == '__main__':
    main()
