import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a = [int(input()) for _ in range(5)]
    k = int(readline())

    if a[4] - a[0] <= k:
        print("Yay!")
    else:
        print(":(")

if __name__ == '__main__':
    main()
