import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = list(map(int, readline().split()))
    s = set(x)

    print(len(s))


if __name__ == '__main__':
    main()
