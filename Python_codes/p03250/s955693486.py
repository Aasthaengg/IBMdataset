import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b, c = map(int, readline().split())
    print(max(a, b, c) * 10 + a + b + c - max(a, b, c))


if __name__ == '__main__':
    main()
