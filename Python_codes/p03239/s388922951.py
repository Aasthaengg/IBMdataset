import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, T = map(int, readline().split())
    ans = INF

    for _ in range(N):
        c, t = map(int, readline().split())
        if t <= T:
            ans = min(ans, c)

    if ans == INF:
        print("TLE")
    else:
        print(ans)


if __name__ == '__main__':
    main()
