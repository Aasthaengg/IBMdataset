import sys

readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    N, M = map(int, input().split())
    time = 1900 * M + 100 * (N - M)
    ans = time * 2 ** M
    print(ans)


if __name__ == '__main__':
    main()
