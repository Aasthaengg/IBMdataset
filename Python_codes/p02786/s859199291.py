import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    H = int(readline())

    cur = 1
    cnt = 1

    while 2 * cur <= H:
        cur *= 2
        cnt *= 2
        cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
