import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    a = list(map(int, readline().split()))
    a.sort(reverse=True)

    x = sum(a[::2])
    y = sum(a[1::2])

    print(x - y)


if __name__ == '__main__':
    main()
