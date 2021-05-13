import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = int(readline())
    s = input()

    if x >= 3200:
        print(s)
    else:
        print("red")


if __name__ == '__main__':
    main()
