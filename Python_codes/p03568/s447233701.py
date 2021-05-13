import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    A = list(map(int, readline().split()))

    ans = 3 ** N
    excl = 1

    for x in A:
        if x % 2 == 0:
            excl *= 2

    ans -= excl

    print(ans)


if __name__ == '__main__':
    main()
