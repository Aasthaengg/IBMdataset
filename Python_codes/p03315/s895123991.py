import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    ans = s.count("+") - s.count("-")
    print(ans)


if __name__ == '__main__':
    main()
