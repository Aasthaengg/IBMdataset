import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    W, a, b = map(int, readline().split())

    if b + W < a:
        print(a - (b + W))
    elif a + W < b:
        print(b - (a + W))
    else:
        print(0)


if __name__ == '__main__':
    main()
