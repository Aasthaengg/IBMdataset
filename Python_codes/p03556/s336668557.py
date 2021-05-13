import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    n = 1
    while (n + 1) * (n + 1) <= N:
        n += 1

    print(n * n)

    return


if __name__ == '__main__':
    main()
