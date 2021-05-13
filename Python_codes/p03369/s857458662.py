import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()

    print(700 + S.count("o") * 100)


if __name__ == '__main__':
    main()
