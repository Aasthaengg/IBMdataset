import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, K = map(int, readline().split())

    cnt = (N + 1) // 2

    if cnt >= K:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
