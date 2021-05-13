import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    A, P = map(int, readline().split())

    print((A * 3 + P) // 2)
    return


if __name__ == '__main__':
    main()
