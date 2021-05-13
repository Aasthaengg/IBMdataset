import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    x, y, z = map(int, readline().split())

    print(x * y // 2)

    return


if __name__ == '__main__':
    main()
