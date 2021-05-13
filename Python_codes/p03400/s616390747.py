import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N = int(readline())
    D, X = map(int, readline().split())
    ans = X

    for _ in range(N):
        a = int(readline())
        for i in range(1, D + 1, a):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
