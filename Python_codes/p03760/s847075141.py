import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import zip_longest

    o = input()
    e = input()

    res = ""
    for a, b in zip_longest(o, e, fillvalue=""):
        res += a
        res += b

    print(res)


if __name__ == '__main__':
    main()
