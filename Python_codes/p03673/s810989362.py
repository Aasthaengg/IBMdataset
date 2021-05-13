import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    a = list(map(int, readline().split()))

    odd = a[0::2]
    even = a[1::2]

    if n % 2 == 0:
        res = even[::-1] + odd
        print(*res)
    else:
        res = odd[::-1] + even
        print(*res)


if __name__ == '__main__':
    main()
