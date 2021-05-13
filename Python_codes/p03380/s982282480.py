import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    A.sort()
    n = max(A)

    i = 0
    while i < N - 2 and 2 * A[i] < n:
        i += 1

    if i in (0, N - 1):
        r = A[i]
    elif abs(2 * A[i] - n) < abs(2 * A[i - 1] - n):
        r = A[i]
    else:
        r = A[i - 1]

    print(n, r)
    return


if __name__ == '__main__':
    main()
