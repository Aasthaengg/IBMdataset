import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = input()

    res = ""
    for x in n:
        res += "9" if x == "1" else "1"

    print(res)


if __name__ == '__main__':
    main()
