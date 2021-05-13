import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from math import comb

    n, p = map(int, readline().split())
    a = list(map(int, readline().split()))

    zero = 0
    one = 0

    for x in a:
        if x % 2 == 0:
            zero += 1
        else:
            one += 1

    ans = 0
    q = 2 ** zero

    if p == 0:
        for x in range(0, one + 1, 2):
            ans += q * comb(one, x)
    else:
        for x in range(1, one + 1, 2):
            ans += q * comb(one, x)

    print(ans)


if __name__ == '__main__':
    main()
