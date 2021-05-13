import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    k = 0

    while k * (k + 1) // 2 < n:
        k += 1

    x = k * (k + 1) // 2
    d = x - n

    for i in range(1, k + 1):
        if i == d:
            continue
        print(i)


if __name__ == '__main__':
    main()
