import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    a, b = map(int, readline().split())

    print((a + b + 1) // 2)

    return


if __name__ == '__main__':
    main()
