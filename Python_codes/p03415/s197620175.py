import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    res = ""

    for i in range(3):
        s = input()
        res += s[i]

    print(res)


if __name__ == '__main__':
    main()
