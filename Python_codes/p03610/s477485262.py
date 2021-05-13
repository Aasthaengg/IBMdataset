import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    print(s[::2])


if __name__ == '__main__':
    main()
