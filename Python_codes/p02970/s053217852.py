import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, D = map(int, readline().split())
    F = 2 * D + 1
    print((N + F - 1) // F)

    return


if __name__ == '__main__':
    main()
