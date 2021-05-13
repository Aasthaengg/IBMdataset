import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import groupby
    s = input()
    ans = len(list(groupby(s))) - 1
    print(ans)


if __name__ == '__main__':
    main()
