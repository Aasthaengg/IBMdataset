import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()

    if len(S) == 3:
        print(S[::-1])
    else:
        print(S)


if __name__ == '__main__':
    main()
