import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    s = input()

    red = s.count("R")
    blue = s.count("B")

    if red > blue:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
