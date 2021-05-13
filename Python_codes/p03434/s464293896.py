import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    A.sort(reverse=True)

    print(sum(A[::2]) - sum(A[1::2]))

    return


if __name__ == '__main__':
    main()
