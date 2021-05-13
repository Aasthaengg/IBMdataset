import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a = int(readline())
    b = int(readline())

    if a > b:
        print("GREATER")
    elif a < b:
        print("LESS")
    else:
        print("EQUAL")


if __name__ == '__main__':
    main()
