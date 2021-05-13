import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    l = len(S)
    x = S.count("o")
    y = 15 - l

    if x + y >= 8:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
