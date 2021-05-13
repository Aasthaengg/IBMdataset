import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b, c = input().split()
    print((a[0] + b[0] + c[0]).upper())


if __name__ == '__main__':
    main()
