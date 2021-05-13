import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def main():
    H, W = map(int, readline().split())
    C = [list(map(int, readline().split())) for _ in range(10)]
    A = list(map(int, read().split()))

    for k in range(10):
        for i in range(10):
            for j in range(10):
                if C[i][j] > C[i][k] + C[k][j]:
                    C[i][j] = C[i][k] + C[k][j]

    ans = 0
    for n in A:
        if n != -1:
            ans += C[n][1]

    print(ans)
    return


if __name__ == '__main__':
    main()
