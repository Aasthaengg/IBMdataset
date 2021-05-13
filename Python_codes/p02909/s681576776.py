import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    S = input()
    p = ["Sunny", "Cloudy", "Rainy"]

    print(p[(p.index(S) + 1) % 3])


if __name__ == '__main__':
    main()
