import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B = map(int, readline().split())

    S = [['#' if i < 50 else '.' for j in range(100)] for i in range(100)]

    for n in range(A - 1):
        q, r = divmod(n, 50)
        S[2 * q + 1][2 * r] = '.'

    for n in range(B - 1):
        q, r = divmod(n, 50)
        S[2 * q + 51][2 * r] = '#'

    print(100, 100)
    for row in S:
        print(''.join(row))

    return


if __name__ == '__main__':
    main()
