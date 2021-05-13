import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M, C = map(int, readline().split())
    B = list(map(int, readline().split()))
    A = [list(map(int, readline().split())) for _ in range(N)]

    ans = 0
    for a in A:
        p = C
        for i in range(M):
            p += a[i] * B[i]
        if p > 0:
            ans += 1

    print(ans)
    return


if __name__ == '__main__':
    main()
