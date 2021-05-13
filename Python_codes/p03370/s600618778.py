import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    N, X = map(int, readline().split())

    m = [int(input()) for _ in range(N)]
    s = sum(m)
    m.sort()

    ans = N + (X - s) // m[0]
    print(ans)

if __name__ == '__main__':
    main()
