import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    L = list(map(int, readline().split()))

    first = max(L)
    second = sum(L) - max(L)

    if first < second:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
