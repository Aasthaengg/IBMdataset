import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = input()
    y = input()

    if x == y[::-1]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
