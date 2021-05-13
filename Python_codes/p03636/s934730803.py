import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    l = len(s) - 2

    print(s[0] + str(l) + s[-1])


if __name__ == '__main__':
    main()
