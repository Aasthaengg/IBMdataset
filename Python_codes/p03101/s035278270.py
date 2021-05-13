import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    H, W, h, w = map(int, read().split())

    print((H - h) * (W - w))

    return


if __name__ == '__main__':
    main()
