import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    a, b, c, d = map(int, readline().split())

    if abs(a - c) <= d or abs(a - b) <= d and abs(b - c) <= d:
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
