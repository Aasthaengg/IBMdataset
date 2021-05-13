import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    A, B, K = map(int, readline().split())

    if B - A + 1 < 2 * K:
        ans = list(range(A, B + 1))
    else:
        ans = list(range(A, A + K)) + list(range(B - K + 1, B + 1))

    print(*ans, sep='\n')

    return


if __name__ == '__main__':
    main()
