import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, H, W = map(int, readline().split())

    ans = 0
    for _ in range(N):
        a, b = map(int, readline().split())
        if H <= a and W <= b:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
