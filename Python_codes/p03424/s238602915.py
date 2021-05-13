import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    S = input().split()

    ans = len(set(S))

    if ans == 4:
        print("Four")
    else:
        print("Three")


if __name__ == '__main__':
    main()
