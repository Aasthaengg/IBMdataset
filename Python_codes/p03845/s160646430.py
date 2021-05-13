import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    T = list(map(int, readline().split()))
    M = int(readline())

    S = sum(T)

    for i in range(M):
        p, x = map(int, readline().split())
        p -= 1

        print(S - T[p] + x)


if __name__ == '__main__':
    main()
